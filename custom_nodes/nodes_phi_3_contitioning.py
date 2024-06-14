class phi_3_conditioning:

    @classmethod
    # nodes in
    def INPUT_TYPES(s):
        return {
            "required": {
                "clip": ("CLIP",),
                "text": ("STRING", {
                    "multiline": True,
                    "default": "Describe a photo of a sunset over a lake."
                }),
                "Enable_Phy_3_Prompt": (["enable", "disable"],),
                }
            }
    
    # nodes out
    RETURN_TYPES = ("CONDITIONING",)

    # OUTPUT_NODE = False
    FUNCTION = "encode"

    CATEGORY = "Example"

    def encode(self, clip, text, Enable_Phy_3_Prompt):
        if Enable_Phy_3_Prompt == "enable":
            tokens = clip.tokenize(text)
            print(type(tokens))
            import torch
            from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
            torch.random.manual_seed(0)
            model = AutoModelForCausalLM.from_pretrained(
                "microsoft/Phi-3-mini-128k-instruct", 
                device_map="cuda", 
                torch_dtype="auto", 
                trust_remote_code=True, 
            )
            tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-128k-instruct")
            messages = [
                {"role": "user", "content": "You are a helpful digital assistant expert in prompt engeneering for stable diffusion."},
                {"role": "user", "content": "Picture of a woman"},
                {"role": "assistant", "content": "a serene and elegant woman, standing confidently in a softly lit room. Her posture is poised and graceful, exuding a sense of calm and stability. She is dressed in a flowing, pastel-colored dress that gently sways with her every movement, reflecting the tranquility of her demeanor. The lighting is warm and inviting, casting a soft glow on her features, highlighting her gentle smile and kind eyes. Her hair is styled in a simple yet sophisticated manner, adding to her overall composed and balanced appearance. This image, rendered at a high resolution of 8k, captures the essence of stability and grace, making her presence both comforting and inspiring."},
                {"role": "user", "content": text},
            ]
            pipe = pipeline(
                "text-generation",
                model=model,
                tokenizer=tokenizer,
            )
            generation_args = {
                "max_new_tokens": 500,
                "return_full_text": False,
                "temperature": 0.0,
                "do_sample": False,
            }
            text_output = pipe(messages, **generation_args)
            print(text)
            generated_text = text_output[0]['generated_text']
            print(generated_text)
            tokens = clip.tokenize(generated_text)
        else:
            tokens = clip.tokenize(text)

        cond, pooled = clip.encode_from_tokens(tokens, return_pooled=True)
        return ([[cond, {"pooled_output": pooled}]], )
        
        
    
NODE_CLASS_MAPPINGS = {
"phi_3_conditioning": phi_3_conditioning
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "phi_3_conditioning": "phi_3_conditioning"
}
