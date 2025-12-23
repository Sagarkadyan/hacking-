import imageio
import sys

# USB forwarded stream from phone
url = "http://127.0.0.1:8080/video"  # your forwarded stream

output_file = 'phone_capture.mp4'

print("Attempting to open stream...")
try:
    with imageio.get_reader(url) as reader:
        print("Stream opened successfully.")
        
        # Get stream properties from metadata
        meta_data = reader.get_meta_data()
        fps = meta_data.get('fps', 20) # fallback to 20 if not available
        
        print(f"Stream properties: FPS={fps}")

        with imageio.get_writer(output_file, fps=fps, codec='libx264') as writer:
            print(f"Recording to {output_file}... Press Ctrl+C to stop.")
            
            for i, frame in enumerate(reader):
                writer.append_data(frame)
                if i % fps == 0: # Print progress once per second
                    sys.stdout.write(f"\rFrames written: {i}")
                    sys.stdout.flush()

except KeyboardInterrupt:
    print("\nStopping recording.")
except Exception as e:
    print(f"\nAn error occurred: {e}")
finally:
    print(f"\nRecording saved as '{output_file}'")