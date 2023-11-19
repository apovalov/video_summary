import openai

def summary_prompt(input_text: str) -> str:
    """
    Build prompt using input text of the video.
    """
    prompt = f"Создайте краткое и информативное описание видео на основе следующего текста:\n{input_text}\n\nКраткое описание:"
    return prompt

def summarize_text(input_text: str) -> str:
    """
    Summarize input text of the video.

    Examples
    --------
    'This video explains...'
    """
    try:
        # Формирование запроса
        prompt = summary_prompt(input_text)

        response = openai.chat.completions.create(
        # response=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7  # Уровень случайности вывода модели
        )

        # Возврат ответа
        return response.choices[0].message.content
        # return response.choices[0].message["content"]
    except Exception as e:
        raise Exception(f"Error in generating summary: {e}")
