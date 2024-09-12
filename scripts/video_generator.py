from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips, concatenate_audioclips
import os
import random


def concatenate_videos_with_audio(input_video_folder, input_audio_folder, output_file):
    # Get all video files from the input folder
    video_files = [f for f in os.listdir(
        input_video_folder) if f.endswith(('.mp4', '.avi', '.mov'))]

    # Get all audio files from the input folder
    audio_files = [f for f in os.listdir(
        input_audio_folder) if f.endswith(('.mp3', '.wav', '.aac'))]

    # Sort the files to ensure consistent order
    random.shuffle(video_files)
    audio_files.sort()

    # Create VideoFileClip objects for each video, removing audio
    video_clips = [VideoFileClip(os.path.join(
        input_video_folder, f)).without_audio() for f in video_files]

    # Create AudioFileClip objects for each audio file
    audio_clips = [AudioFileClip(os.path.join(
        input_audio_folder, f)) for f in audio_files]

    # Concatenate the video clips
    final_video = concatenate_videoclips(video_clips)

    # Concatenate the audio clips
    final_audio = concatenate_audioclips(audio_clips)

    # Adjust the duration of the video to match the audio
    if final_video.duration > final_audio.duration:
        final_video = final_video.subclip(0, final_audio.duration)
    else:
        # If video is shorter, loop it to match audio duration
        final_video = final_video.loop(duration=final_audio.duration)

    # Set the audio of the final clip
    final_clip = final_video.set_audio(final_audio)

    # Write the result to a file
    final_clip.write_videofile(output_file, codec="libx264")

    # Close all clips
    final_clip.close()
    final_video.close()
    final_audio.close()
    for clip in video_clips:
        clip.close()
    for clip in audio_clips:
        clip.close()
