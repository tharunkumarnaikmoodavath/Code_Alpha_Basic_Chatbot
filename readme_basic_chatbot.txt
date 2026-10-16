========================================================================
                         BASIC PYTHON CHATBOT
========================================================================

DESCRIPTION
-----------
This is a simple, rule-based command-line chatbot written in Python. 
It listens to user input in an interactive loop, processes common text 
phrases, and responds dynamically until the user exits the session.

FEATURES
--------
- Command-line interactive chat interface.
- Case-insensitive input matching.
- Predefined responses for greetings, status checks, and farewells.
- Fallback response for unrecognized user queries.
- Clean session termination upon receiving the exit command.

REQUIREMENTS
------------
- Python 3.x installed on your system.

HOW TO RUN
----------
1. Open your terminal or command prompt.
2. Navigate to the directory containing 'BASIC CHATBOT.py':
   
   cd path/to/your/folder

3. Run the Python script:

   python "BASIC CHATBOT.py"

USAGE / EXAMPLE INTERACTION
---------------------------
When prompted with "You: ", enter one of the following supported phrases:

- "hello"       --> Bot replies: "Hi!"
- "how are you" --> Bot replies: "I'm fine,thanks!"
- "bye"         --> Bot replies: "Goodbye!" and ends the program.
- Any other text --> Bot replies: "Sorry, I don't understand."

Example Session:
----------------
===== BASIC CHATBOT =====
You: hello
Hi!
You: how are you
I'm fine,thanks!
You: what is your name
Sorry, I don't understand.
You: bye
Goodbye!

LICENSE
-------
This project is open-source and available under the MIT License.
========================================================================