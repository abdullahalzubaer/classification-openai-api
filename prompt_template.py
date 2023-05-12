
# Note on PROMPT_TEMPLATE_4_SHOT_COT - the 4 shot is chosen from PROMPT_TEMPLATE_4SHOT, it will allow us to compare the peformance between 
# PROMPT_TEMPLATE_4SHOT and PROMPT_TEMPLATE_4_SHOT_COT.
PROMPT_TEMPLATE_4_SHOT_COT=f"""In this task, you will be given a text and your goal is to classify the text as either "Hate speech" or "Not hate speech" based on its linguistic content. You must also provide a brief explanation of why you think so and only then provide the classification label.

Output format will be as follows:

Explanation:
Classification:

Definition:

-Hate speech: Text that contains derogatory, offensive, or discriminatory language targeting individuals or groups based on their race, ethnicity, gender, religion, sexual orientation, or other protected characteristics. t may include explicit slurs, threats, expressions of violence, dehumanization, or incitement of hatred towards a particular group.

-Not hate speech: Text that does not contain derogatory, offensive, or discriminatory language targeting individuals or groups based on their race, ethnicity, gender, religion, sexual orientation, or other protected characteristics. It may include casual language, humor, or general statements without promoting hate or harm, or discriminatory behavior.

Below are example of "Hate speech" and "Not hate speech"

Example:
Classification:

Example:
Classification:

Example:
Classification:

Example:
Classification:

Text to classify:[TEST_TEXT]
Explanation:"""

PROMPT_TEMPLATE_ZEROSHOT=f"""In this task, you will be given a text and your goal is to classify the text as either "Hate speech" or "Not hate speech" based on its linguistic content.

Definition:

-Hate speech: Text that contains derogatory, offensive, or discriminatory language targeting individuals or groups based on their race, ethnicity, gender, religion, sexual orientation, or other protected characteristics. t may include explicit slurs, threats, expressions of violence, dehumanization, or incitement of hatred towards a particular group.

-Not hate speech: Text that does not contain derogatory, offensive, or discriminatory language targeting individuals or groups based on their race, ethnicity, gender, religion, sexual orientation, or other protected characteristics. It may include casual language, humor, or general statements without promoting hate or harm, or discriminatory behavior.

Text to classify:[TEST_TEXT]
Classification:"""


PROMPT_TEMPLATE_2SHOT=f"""In this task, you will be given a text and your goal is to classify the text as either "Hate speech" or "Not hate speech" based on its linguistic content.

Definition:

-Hate speech: Text that contains derogatory, offensive, or discriminatory language targeting individuals or groups based on their race, ethnicity, gender, religion, sexual orientation, or other protected characteristics. t may include explicit slurs, threats, expressions of violence, dehumanization, or incitement of hatred towards a particular group.

-Not hate speech: Text that does not contain derogatory, offensive, or discriminatory language targeting individuals or groups based on their race, ethnicity, gender, religion, sexual orientation, or other protected characteristics. It may include casual language, humor, or general statements without promoting hate or harm, or discriminatory behavior.

Below are examples of "Hate speech" and "Not hate speech"

Example:
Classification:

Example:
Classification:

Text to classify:[TEST_TEXT]
Classification:"""


PROMPT_TEMPLATE_4SHOT=f"""In this task, you will be given a text and your goal is to classify the text as either "Hate speech" or "Not hate speech" based on its linguistic content.

Definition:

-Hate speech: Text that contains derogatory, offensive, or discriminatory language targeting individuals or groups based on their race, ethnicity, gender, religion, sexual orientation, or other protected characteristics. t may include explicit slurs, threats, expressions of violence, dehumanization, or incitement of hatred towards a particular group.

-Not hate speech: Text that does not contain derogatory, offensive, or discriminatory language targeting individuals or groups based on their race, ethnicity, gender, religion, sexual orientation, or other protected characteristics. It may include casual language, humor, or general statements without promoting hate or harm, or discriminatory behavior.

Below are examples of "Hate speech" and "Not hate speech"

Example:
Classification:

Example:
Classification:

Example:
Classification:

Example:
Classification:

Text to classify:[TEST_TEXT]
Classification:"""



PROMPT_TEMPLATE_8SHOT=f"""In this task, you will be given a text and your goal is to classify the text as either "Hate speech" or "Not hate speech" based on its linguistic content.

Definition:

-Hate speech: Text that contains derogatory, offensive, or discriminatory language targeting individuals or groups based on their race, ethnicity, gender, religion, sexual orientation, or other protected characteristics. t may include explicit slurs, threats, expressions of violence, dehumanization, or incitement of hatred towards a particular group.

-Not hate speech: Text that does not contain derogatory, offensive, or discriminatory language targeting individuals or groups based on their race, ethnicity, gender, religion, sexual orientation, or other protected characteristics. It may include casual language, humor, or general statements without promoting hate or harm, or discriminatory behavior.


Example:
Classification:

Example:
Classification:

Example:
Classification:

Example:
Classification:

Example:
Classification:

Example:
Classification:

Example:
Classification:

Example:
Classification:

Text to classify:[TEST_TEXT]
Classification:"""


def create_prompt(test_text, zeroshot=False, twoshot=False, fourshot=False, eightshot=False, fourshotcot=False):
    '''
    Create a prompt based on the provided test_text and options.

    Parameters:
    - test_text (str): The test sentence.
    - zeroshot (bool): Flag indicating whether to use the zero-shot prompt template.
    - cot (bool): Flag indicating whether to use the cot prompt template.
    - twoshot (bool): Flag indicating whether to use the 2-shot prompt template.
    - fourshot (bool): Flag indicating whether to use the 4-shot prompt template.
    - eightshot (bool): Flag indicating whether to use the 8-shot prompt template.

    Returns:
    - str: The generated prompt.
    '''

    if zeroshot:
        return PROMPT_TEMPLATE_ZEROSHOT.replace("[TEST_TEXT]", test_text)
    elif twoshot:
        return PROMPT_TEMPLATE_2SHOT.replace("[TEST_TEXT]", test_text)
    elif fourshot:
        return PROMPT_TEMPLATE_4SHOT.replace("[TEST_TEXT]", test_text)
    elif eightshot:
        return PROMPT_TEMPLATE_8SHOT.replace("[TEST_TEXT]", test_text)
    elif fourshotcot:
        return PROMPT_TEMPLATE_4_SHOT_COT.replace("[TEST_TEXT]", test_text)
    else:
        raise ValueError("Please provide a valid flag and be happy: 'zeroshot', 'twoshot', 'fourshot', 'eightshot' or 'fourshotcot'.")

