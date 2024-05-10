from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

systemContent = """
  classify a piece of text into one of the following sensitivity levels: Public Data, Confidential Data, Secret Data, Top Secret Data.

  Instructions:
  Public Data: This category includes information that is publicly available and does not pose any risk if disclosed. Examples include general knowledge, publicly released documents, and information available on public websites.
  Confidential Data: This category encompasses information that is sensitive and should be protected from unauthorized access or disclosure. It may include proprietary information, internal company data, or personal information not meant for public dissemination.
  Secret Data: This category involves highly sensitive information that, if disclosed, could cause significant harm to individuals, organizations, or national security. Examples include classified documents, trade secrets, or sensitive financial data.
  Top Secret Data: This category contains the most sensitive information, the disclosure of which could result in severe consequences, including endangering lives, compromising national security, or causing irreparable damage. Examples include classified intelligence, military strategies, or highly confidential government operations.
  Your task is to utilize the ChatGPT API to accurately classify the given text into one of these four categories based on its sensitivity level. You can provide the input text to the API and expect a classification output indicating the appropriate sensitivity level. the text delimited by triple quotes in 3 bullet points
"""

def get_classification(content):
    completion = client.chat.completions.create(
        model="gpt-4-turbo-2024-04-09",
        messages=[
            {"role": "system", "content": systemContent},
            {"role": "user", "content": content}
        ],
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content
