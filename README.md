### Comprehensive Guide for Using the Text-to-Speech Node and Saving Audio to DaVinci Resolve Studio
## These nodes don't work with the free version of DaVinci Resolve.

How to use the Text-to-Speech (TTS) node and save the generated audio to DaVinci Resolve Studio using ComfyUI. This guide will walk you through each step, ensuring you can leverage this powerful integration effectively.

#### Prerequisites
1. **ComfyUI** installed on your machine.
2. **DaVinci Resolve Studio** installed and running.
3. Basic understanding of how to use nodes in ComfyUI.
4. Access to OpenAI API for voice generation (optional, if not using default voices).
5. Install OpenAI API via pip

---

### Step-by-Step Guide

#### 1. Setting Up the Text-to-Speech Node

1. **Open DaVinci Resolve Studio**:
   Launch DaVinci Resolve Studio on your machine and ensure it is running before proceeding with ComfyUI.

2. **Open ComfyUI**:
   Launch ComfyUI on your machine.

3. **Create a New Node**:
   Navigate to the node creation interface in ComfyUI.

4. **Add the Text-to-Speech Node**:
   - Locate the TTS node in the node library.
   - Drag and drop the TTS node into your workspace.

5. **Configure the TTS Node**:
   - **Text Input**: Enter the text you want to convert to speech.
   - **Voice Selection**: Choose a voice from the available options. If using OpenAI API, ensure you have your API key set up and select a voice from the OpenAI API list.
   - **File Name**: Specify the name for the output audio file.

6. **Output Directory**:
   - The files will be saved in the default output directory of ComfyUI.

#### 2. Generating the Audio File

1. **Queue the Node**:
   - Connect the TTS node to Save Audio To DaVinci
   - Click the ‘Queue’ button to start the process.

2. **Monitor Progress**:
   - Wait for the node to process the text and generate the audio file.
   - Once completed, the audio file will be imported in the active folder in DaVinci.

#### 3. Additional Tips

- **Batch Processing**: You can create multiple TTS nodes if you need to generate and import multiple audio files.
- **Voice Customization**: Explore different voices and settings in the TTS node to find the best fit for your project.
---

### Example Workflow

Here’s an example workflow to illustrate the process:

1. **Setup**:
   - Open DaVinci Resolve Studio.
   - Add a TTS node in ComfyUI.
   - Enter text: “Hello, this is a demo speech for DaVinci Resolve Studio.”
   - Choose a voice: OpenAI's ‘en-US-Wavenet-D’.
   - Set file name: `demo_speech`.

2. **Queue and Generate**:
   - Queue the TTS node.
   - Wait for the audio file to be generated and imported.
---

### Troubleshooting

- **Audio Not Generated**: Ensure all node settings are correctly configured and the output directory is writable.
- **API Issues**: If using OpenAI API, ensure your API key is valid and you have sufficient credits.

---

Happy editing!

Contributing

