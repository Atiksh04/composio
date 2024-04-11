## Automated code quality and commit names checker

This repository contains code for automated Code quality and commit names checker.
I've used composio Github integration for this.

The process works as follows:
1. A user creates a Pull Request (PR).
2. We receive a webhook event from Composio, allowing us to access the PR contents.
3. If the PR does not meet quality standards, we automatically generate a GitHub issue highlighting the areas that need attention.


Here's a Video demostrating the same: 
Drive link: [https://drive.google.com/file/d/1aJKUVYm203GAnGeRUnmdNaozm28eZT01/view?usp=sharing]



## Steps to run this applications:

1. Clone this repository
2. Create a `.env` file and add OPENAI_SECRET and COMPOSIO_KEY
3. Navigate to this folder and hit `python run.py`


## Below is the same output that we get in the video:

" Reviewing the file changes in the pull request and the commit names, here is the analysis based on the provided rules:

File Changes Review:
1. **No print statements allowed**:
   - **Invalid**: The file `app/llm_handler/composio_autogen.py` contains a print statement `print(response.chat_history)`.
   - **Invalid**: The file `app/routes.py` contains a print statement `print ("asdas")`.

2. **Comments must accompany each added function**:
   - **Invalid**: The addition in the file `app/handler.py` defines the function `get_hello_handler()` without an accompanying comment.
   - **Invalid**: The addition in the file `app/llm_handler/composio_autogen.py` defines the function `trigger_task()` without an accompanying comment.
   - **Invalid**: The addition in the file `app/routes.py` with the function `handle_trigger_endpoint()` lacks comments.

3. **Eliminate unused variables**.
   - Unable to validate without the full file context to check for unused variables.

4. **Ensure line lengths do not exceed 250 characters for readability**:
   - Review shows no lines exceeding 250 characters in the provided patches.

5. **Enumerate valid and invalid steps accordingly**:
   - Valid: Patches indicate correct addition of new files and functions.
   - Invalid: Lack of comments, presence of print statements, and potential unused variables as mentioned in the points above.

Commit Names Review:
1. **Commit names begin with keywords 'added' or 'removed'**:
   - **Invalid**: The commit with SHA `7b1843de9888d9bb5a2a26c3ea1a0bf7da065762` does not follow the naming convention.
   - **Valid**: The commit with SHA `e73b78390ad887bf2205e96b265ff6ee6c92a526` starts with "added: basic changes".
   - **Invalid**: The commit with SHA `62bac370f6f2750047ce62b5b242f7aac33dabca` does not follow the naming convention.

Given the above analysis, there are several non-compliant elements within the PR. A GitHub issue should be created to address the violations of the specified rules. "
