# AutoName

**autoName** is a Python application for generating usernames that are resistant to OSINT (Open Source Intelligence) attacks. It helps users select usernames that blend in with common words or already-used names, making it harder to fingerprint or track users based on their usernames.

## Features

- **Common Word Usernames:** Generate usernames from a list of common words.
- **Already Used Names:** Generate usernames that are already in use by others, hiding in the "shadow" of existing users.
- **Common Word + Already Used:** Combine both strategies for maximum anonymity.
- **Avoids Duplicates:** Ensures generated usernames are not already in use by the current user.

## How It Works

The application uses several JSON files to manage pools of usernames:
- `commonWord_one.json`: List of common words.
- `alreadyUsedName_two.json`: List of usernames already in use.
- `commonWordAlreadyUsedName_three.json`: List of common words that are also already used as usernames.
- `inUseName.json`: Tracks usernames currently in use by the user to avoid duplicates.

When you run the app, you can choose one of three strategies for generating a username. The app will randomly select a username from the appropriate list, ensuring it is not already in use by you.

## Configuration

1. **Edit JSON Files:**
   - Update the JSON files (`commonWord_one.json`, `alreadyUsedName_two.json`, `commonWordAlreadyUsedName_three.json`, `inUseName.json`) to add or remove words/usernames as needed.
   - Make sure the JSON structure matches the examples provided in the repository.

2. **Run the Application:**
   - Make sure you have Python 3 installed.
   - No external dependencies are required.
   - Run the application with:
     ```sh
     python3 main.py
     ```

3. **Follow Prompts:**
   - Choose your desired username generation strategy when prompted.
   - The generated username will be displayed if it is not already in use.

## Example JSON Structure

**commonWord_one.json**
```json
{
  "commonWords": ["the", "be", "to", "of", "and", "a", ...]
}
```

**alreadyUsedName_two.json**
```json
{
  "takenUsernames": ["john", "jane", "guest", "test", ...]
}
```

**commonWordAlreadyUsedName_three.json**
```json
{
  "commonWordAlreadyUsedName": ["john", "the", "alpha", ...]
}
```

**inUseName.json**
```json
{
  "inUseNames": ["the", "janeDoe", "coolguy42", ...]
}
```

## Notes

- The application does not require any third-party Python packages.
- To add more username sources or logic, edit the JSON files or the Python code as needed.

---

**Author:**
elizabeth325

---

⚠️ Disclaimer

This project is intended for educational and research purposes only.
It is not designed or intended for malicious use, and the author does not condone or support any illegal or unethical behavior related to the use of this code.
Use responsibly and in compliance with all applicable laws and regulations.
