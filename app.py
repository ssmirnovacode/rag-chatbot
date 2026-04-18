import gradio as gr
from dotenv import load_dotenv
from answer import answer_question

load_dotenv(override=True)

# ---------- Helpers ----------


def format_context(context):
    if not context:
        return ""

    blocks = []
    for doc in context:
        blocks.append(
            f"""
        <div style='padding:12px;margin-bottom:10px;border-radius:12px;background:#1f1f1f;'>
            <div style='font-size:12px;color:#aaa;margin-bottom:6px;'>📄 {doc.metadata.get('source','unknown')}</div>
            <div style='font-size:14px;line-height:1.5;'>{doc.page_content}</div>
        </div>
        """
        )

    return "<h3 style='margin-bottom:10px;'>📚 Retrieved Context</h3>" + "".join(blocks)


def chat(history):
    last_message = history[-1]["content"]
    prior = history[:-1]

    answer, context = answer_question(last_message, prior)

    history.append({"role": "assistant", "content": answer})
    return history, format_context(context)


def put_message(message, history):
    return "", history + [{"role": "user", "content": message}]


# ---------- UI ----------


def main():
    theme = gr.themes.Soft(
        primary_hue="orange",
        radius_size="lg",
        font=["Inter", "system-ui", "sans-serif"],
    )

    with gr.Blocks(theme=theme, title="RAG Chat") as ui:

        gr.HTML(
            """
        <div style='text-align:center;margin-bottom:10px;'>
            <h1 style='margin-bottom:5px;'>🧠 RAG Assistant</h1>
            <p style='color:#aaa;'>Ask questions based on your documents</p>
        </div>
        """
        )

        with gr.Row():
            with gr.Column(scale=3):
                chatbot = gr.Chatbot(
                    height=600,
                    bubble_full_width=False,
                    show_copy_button=True,
                    avatar_images=(
                        None,
                        "https://cdn-icons-png.flaticon.com/512/4712/4712027.png",
                    ),
                    type="messages",
                )

                with gr.Row():
                    message = gr.Textbox(
                        placeholder="Type your question...",
                        show_label=False,
                        scale=8,
                        container=True,
                    )
                    send_btn = gr.Button("➤", scale=1)

            with gr.Column(scale=2):
                context_box = gr.HTML(
                    "<div style='color:#777;'>Context will appear here</div>",
                    elem_id="context-box",
                )

        # ---------- Interactions ----------

        message.submit(
            put_message,
            inputs=[message, chatbot],
            outputs=[message, chatbot],
        ).then(chat, inputs=chatbot, outputs=[chatbot, context_box])

        send_btn.click(
            put_message,
            inputs=[message, chatbot],
            outputs=[message, chatbot],
        ).then(chat, inputs=chatbot, outputs=[chatbot, context_box])

    ui.launch(inbrowser=True)


if __name__ == "__main__":
    main()
