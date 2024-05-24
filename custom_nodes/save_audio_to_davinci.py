import folder_paths
import os
import sys

os.environ["RESOLVE_SCRIPT_API"] = "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting"
os.environ["RESOLVE_SCRIPT_LIB"] = "/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/fusionscript.so"
sys.path.append(os.path.join(os.environ["RESOLVE_SCRIPT_API"], "Modules"))
import DaVinciResolveScript as dvr_script

class SaveAudioToDaVinci:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "audio_path": ("AUDIO", ),
                "filename_prefix": ("STRING", {"default": "ComfyUI"}),
            },
        }
    RETURN_TYPES = ()
    FUNCTION = "save_audio"

    OUTPUT_NODE = True

    CATEGORY = "audio"

    def save_audio(self, audio_path, filename_prefix):
        try:
            if not audio_path or not os.path.exists(audio_path):
                print(f"Invalid audio path: {audio_path}")
                return {}

            full_output_folder, filename, counter, subfolder, filename_prefix = folder_paths.get_save_image_path(filename_prefix, self.output_dir, 0, 0)
            audio_output_path = os.path.join(full_output_folder, os.path.basename(audio_path))
            
            os.makedirs(full_output_folder, exist_ok=True)
            os.rename(audio_path, audio_output_path)

            resolve = dvr_script.scriptapp("Resolve")
            project = resolve.GetProjectManager().GetCurrentProject()
            media_pool = project.GetMediaPool()

            if media_pool.ImportMedia([audio_output_path]):
                print(f"Audio file imported successfully: {audio_output_path}")
            else:
                print(f"Failed to import audio file: {audio_output_path}")

            return {"audio_path": audio_output_path}
        except Exception as e:
            print(f"An error occurred while importing audio to DaVinci: {e}")
            return {"error": str(e)}

NODE_CLASS_MAPPINGS = {
    "SaveAudioToDaVinci": SaveAudioToDaVinci
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SaveAudioToDaVinci": "Save Audio to DaVinci"
}
