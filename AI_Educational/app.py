# Import necessary libraries
from g4f.client import Client
import gradio as gr

# Initialize the G4F client
client = Client()

# Define the function for generating educational content
def generate_educational_content(subject):
    # Generate summary using the model
    summary_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that responds in English."},
            {"role": "user", "content": f"Provide a detailed material and resource of the topic: {subject}"}],
    )
    summary = summary_response.choices[0].message.content

    # Generate questions using the model
    questions_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that responds in English."},
            {"role": "user", "content": f"Generate 10 questions in English about the topic: {subject}"}],
    )
    questions = questions_response.choices[0].message.content

    return f"Summary:\n{summary}\n\nQuestions:\n{questions}"

# Gradio user interface
interface = gr.Interface(
    fn=generate_educational_content,
    inputs=gr.Textbox(lines=3, placeholder="Enter a subject, e.g., gravitation, Least Common Multiple, Virus..."),
    outputs="text",
    title="Educational Assistant 📚",
    description="Get a summary and questions for any subject. Enhance your learning with concise explanations and relevant questions.",
    theme="huggingface",
    examples=[
        ["gravitation"],
        ["least common multiple"],
        ["virus"],
    ],
    css="""
    body {font-family: 'Arial', sans-serif; background-color: #f9f9f9; color: #333;}
    .container {max-width: 700px; margin: auto; padding: 20px; background-color: #fff; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);}
    h1 {text-align: center; color: #4CAF50;}
    .gr-button {background-color: #4CAF50; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; transition-duration: 0.4s; cursor: pointer;}
    .gr-button:hover {background-color: white; color: black; border: 2px solid #4CAF50;}
    input[type=text] {width: 100%; padding: 12px 20px; margin: 8px 0; display: inline-block; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;}
    """
)

# Launch the interface
if __name__ == "__main__":
    interface.launch()

