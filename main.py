from utils import read_video,save_video
from view_transformer import ViewTransformer
from Speed_and_distance_estimator import SpeedAndDistanceEstimator
import numpy as np
from trackers import Tracker
from team_assigner import TeamAssigner
import cv2
from player_ball_assigner import PlayerBallAssigner
from Camera_movement import CameraMovementEstimator
def main():
    #read_video
    video_frames = read_video('input_videos\\08fd33_0.mp4')

    
    #Initialize Tracker
    tracker = Tracker("Models/best.pt")

    tracks =tracker.get_object_tracks(video_frames,read_from_stub=True
                                      ,stub_path='stubs/tracks_stubs.pkl')
    #Get object postion
    tracker.add_position_to_tracks(tracks)
    
    # camer movement estimator
    camer_estimator =CameraMovementEstimator(video_frames[0])
    camer_movement_per_frame = camer_estimator.get_camera_movement(video_frames,read_from_stub=True,stub_path="stubs/camer_movement.pkl")
    
    camer_estimator.add_adjust_positions_to_tracks(tracks,camer_movement_per_frame)
    
    
    
    # View Transformer
    view_transformer = ViewTransformer()
    view_transformer.add_transformed_position_to_tracks(tracks)
    

    # Speed and Distance Estimator
    speedAndDistanceEstimator = SpeedAndDistanceEstimator()
    speedAndDistanceEstimator.add_speed_and_distance_to_tracks(tracks)

    
    # Interpolate Ball postion
    tracks["ball"] = tracker.interpolate_ball_positions(tracks["ball"])
     
  

   # Assign player Teams
    team_assignr =TeamAssigner()
    team_assignr.assign_team_color(video_frames[500],tracks["players"][1])

    for frame_num,player_track in enumerate(tracks["players"]):
        for player_id ,track in player_track.items():
            team = team_assignr.get_player_team(video_frames[frame_num],track['bbox'],player_id)
            tracks['players'][frame_num][player_id]['team'] = team
            tracks['players'][frame_num][player_id]['team_color'] = team_assignr.team_colors[team]

    
   #Assign Ball Aquisition 
    player_assignr = PlayerBallAssigner()
    team_ball_control = []
    for frame_num,player_track in enumerate(tracks["players"]):
        ball_bbox = tracks["ball"][frame_num][1]["bbox"]
        assigned_player = player_assignr.assign_ball_to_player(player_track,ball_bbox)

        if assigned_player != -1:
            tracks["players"][frame_num][assigned_player]["has_ball"] = True
            team_ball_control.append(tracks["players"][frame_num][assigned_player]['team'])
        else:
            team_ball_control.append(team_ball_control[-1])
    team_ball_control = np.array(team_ball_control)
   
   
   #draw object Track
    output_video_frames = tracker.draw_annotations(video_frames,tracks,team_ball_control)
    # draw Cmaera movement 
    output_video_frames = camer_estimator.draw_camera_movement(output_video_frames,camera_movement_per_frame=camer_movement_per_frame)

    #draw speed and distance estimator
    output_video_frames =speedAndDistanceEstimator.draw_speed_and_distance(output_video_frames,tracks)
    # save_video
    save_video(output_video_frames,'output_videos/output_video.avi')
    
if __name__ == "__main__":
    main()