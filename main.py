import os
import time
import sys
import random
from colorama import init, Fore, Back, Style

# Initialize colorama with autoreset=True to automatically reset colors
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_effect(text, delay=0.03, color=Fore.WHITE):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print(Style.RESET_ALL)

def color_fade(text, start_color, end_color):
    for i in range(len(text)):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * i / len(text))
        g = int(start_color[1] + (end_color[1] - start_color[1]) * i / len(text))
        b = int(start_color[2] + (end_color[2] - start_color[2]) * i / len(text))
        sys.stdout.write(f"\033[38;2;{r};{g};{b}m{text[i]}")
        sys.stdout.flush()
        time.sleep(0.005)
    print(Style.RESET_ALL)

def display_header():
    header = """
    ╔══════════════════════════════════════════╗
    ║                 tucot9                   ║
    ║    German Developer, AI Specialist,      ║
    ║        and Cybersecurity Expert          ║
    ╚══════════════════════════════════════════╝
    """
    color_fade(header, (255, 0, 0), (100, 0, 0))

def display_menu():
    print(Fore.RED + "\nMenu:")
    print(Fore.WHITE + "1. About Me")
    print("2. Skills")
    print("3. Projects")
    print("4. Contact")
    print("5. ASCII Art Generator")
    print("6. Matrix Rain Effect")
    print("7. Exit")

def animate_loading():
    chars = "▁▂▃▄▅▆▇█▇▆▅▄▃▂▁"
    for _ in range(2):
        for char in chars:
            sys.stdout.write(f"\r{Fore.RED}Loading {char}")
            sys.stdout.flush()
            time.sleep(0.05)
    print(Style.RESET_ALL)

def about_me():
    clear_screen()
    display_header()
    print_with_effect("About Me:", color=Fore.RED)
    print_with_effect("As a passionate developer from Germany, I specialize in AI development,")
    print_with_effect("automation tools, and cybersecurity. With over a decade of experience")
    print_with_effect("in the tech industry, I've honed my skills in creating cutting-edge")
    print_with_effect("solutions that push the boundaries of what's possible in software development.")
    print()
    print_with_effect("NexusNG AI:", color=Fore.RED)
    print_with_effect("I'm the founder and creator of NexusNG AI, a revolutionary artificial")
    print_with_effect("intelligence assistant that's changing the landscape of software development.")
    print()
    print_with_effect("T9 Group:", color=Fore.RED)
    print_with_effect("As a proud member of the elite T9 group, I collaborate with some of the")
    print_with_effect("brightest minds in the industry to tackle complex challenges and innovate")
    print_with_effect("in the fields of AI and security.")
    input(f"\n{Fore.RED}Press Enter to return to the menu...")

def skills():
    clear_screen()
    display_header()
    skills_list = [
        "Artificial Intelligence", "Machine Learning", "Natural Language Processing",
        "Cybersecurity", "Ethical Hacking", "Automation",
        "Full-Stack Development", "Cloud Computing", "DevOps"
    ]
    print_with_effect("Skills:", color=Fore.RED)
    for skill in skills_list:
        print_with_effect(f"• {skill}", delay=0.05)
        time.sleep(0.2)
    input(f"\n{Fore.RED}Press Enter to return to the menu...")

def projects():
    clear_screen()
    display_header()
    projects_dict = {
        "NexusNG": "An advanced AI assistant for coding and software creation.",
        "SpoofMail": "A powerful email security testing tool.",
        "SecureScript": "A security auditing tool for ethical hackers and Roblox developers."
    }
    print_with_effect("Projects:", color=Fore.RED)
    for project, description in projects_dict.items():
        print_with_effect(f"{project}:", color=Fore.RED)
        print_with_effect(f"{description}")
        print_with_effect("=" * 50, color=Fore.RED)
        time.sleep(0.5)
    input(f"\n{Fore.RED}Press Enter to return to the menu...")

def contact():
    clear_screen()
    display_header()
    print_with_effect("Contact Information:", color=Fore.RED)
    contacts = [
        ("Discord", "tucot9"),
        ("Website", "https://bio.tucot9.com"),
        ("GitHub", "https://github.com/T9Tuco"),
        ("NexusNG", "https://nexusng.site")
    ]
    for platform, info in contacts:
        print_with_effect(f"{platform}: {info}", color=Fore.WHITE)
        time.sleep(0.3)
    input(f"\n{Fore.RED}Press Enter to return to the menu...")

def ascii_art_generator():
    clear_screen()
    display_header()
    print_with_effect("ASCII Art Generator", color=Fore.RED)
    print_with_effect("Enter a word or short phrase to convert to ASCII art:", color=Fore.WHITE)
    
    user_input = input(f"{Fore.GREEN}> {Fore.WHITE}")
    
    fonts = {
        'standard': [
            "  ###   ", " #   #  ", "#     # ", "#     # ", "#     # ", " #   #  ", "  ###   "
        ],
        'block': [
            "███████╗", "██╔════╝", "█████╗  ", "██╔══╝  ", "███████╗", "╚══════╝", "        "
        ],
        'slim': [
            " ┌─┐ ", " ├─┤ ", " └─┘ ", "     ", "     ", "     ", "     "
        ]
    }
    
    print_with_effect("Choose a font style:", color=Fore.RED)
    for i, font in enumerate(fonts.keys(), 1):
        print(f"{i}. {font}")
    
    font_choice = input(f"{Fore.GREEN}Enter your choice (1-3): {Fore.WHITE}")
    font_name = list(fonts.keys())[int(font_choice) - 1]
    font = fonts[font_name]
    
    print_with_effect("Choose a color:", color=Fore.RED)
    colors = [
        (Fore.RED, "Red"), (Fore.GREEN, "Green"), (Fore.BLUE, "Blue"),
        (Fore.YELLOW, "Yellow"), (Fore.MAGENTA, "Magenta"), (Fore.CYAN, "Cyan"),
        (Fore.WHITE, "White")
    ]
    for i, (color, name) in enumerate(colors, 1):
        print(f"{i}. {color}{name}{Style.RESET_ALL}")
    
    color_choice = input(f"{Fore.GREEN}Enter your choice (1-7): {Fore.WHITE}")
    chosen_color, color_name = colors[int(color_choice) - 1]
    
    clear_screen()
    display_header()
    print_with_effect(f"ASCII Art - Font: {font_name}, Color: {color_name}", color=Fore.RED)
    print()
    
    for line in range(len(font)):
        for char in user_input.upper():
            if char.isalpha():
                index = ord(char) - ord('A')
                print(chosen_color + font[line][index % len(font[line])] * 3, end="")
            else:
                print("   ", end="")
        print()
    
    input(f"\n{Fore.RED}Press Enter to return to the menu...")

def matrix_rain_effect():
    clear_screen()
    display_header()
    print_with_effect("Matrix Rain Effect", color=Fore.GREEN)
    
    print_with_effect("Choose a color:", color=Fore.RED)
    colors = [
        (Fore.GREEN, "Green"), (Fore.RED, "Red"), (Fore.BLUE, "Blue"),
        (Fore.YELLOW, "Yellow"), (Fore.MAGENTA, "Magenta"), (Fore.CYAN, "Cyan"),
        (Fore.WHITE, "White")
    ]
    for i, (color, name) in enumerate(colors, 1):
        print(f"{i}. {color}{name}{Style.RESET_ALL}")
    
    color_choice = input(f"{Fore.GREEN}Enter your choice (1-7): {Fore.WHITE}")
    chosen_color, color_name = colors[int(color_choice) - 1]
    
    print_with_effect("Enter custom characters (leave blank for default):", color=Fore.RED)
    custom_chars = input(f"{Fore.GREEN}> {Fore.WHITE}")
    if not custom_chars:
        custom_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()"
    
    print_with_effect("Enter rain speed (1-10, default is 5):", color=Fore.RED)
    speed = input(f"{Fore.GREEN}> {Fore.WHITE}")
    speed = int(speed) if speed.isdigit() and 1 <= int(speed) <= 10 else 5
    delay = 0.1 - (speed * 0.01)
    
    width = os.get_terminal_size().columns
    height = os.get_terminal_size().lines
    
    drops = [0] * width
    screen = [[' ' for _ in range(width)] for _ in range(height)]
    
    print_with_effect(f"Matrix Rain Effect - Color: {color_name}, Speed: {speed}", color=chosen_color)
    print_with_effect("Press Ctrl+C to stop", color=chosen_color)
    time.sleep(2)
    
    try:
        while True:
            # Move existing characters down
            for i in range(height-1, 0, -1):
                for j in range(width):
                    screen[i][j] = screen[i-1][j]
            
            # Generate new characters at the top
            for i in range(width):
                if drops[i] > 0:
                    screen[0][i] = random.choice(custom_chars)
                    drops[i] += 1
                    if drops[i] > height:
                        drops[i] = 0
                elif random.random() > 0.99:
                    screen[0][i] = random.choice(custom_chars)
                    drops[i] = 1
                else:
                    screen[0][i] = ' '
            
            # Clear screen and print the updated matrix
            clear_screen()
            for row in screen:
                print(chosen_color + ''.join(row))
            
            time.sleep(delay)
    except KeyboardInterrupt:
        pass
    
    input(f"\n{Fore.RED}Press Enter to return to the menu...")

def main():
    os.system('title tucot9 - Developer Portfolio')
    animate_loading()
    while True:
        clear_screen()
        display_header()
        display_menu()
        choice = input(Fore.GREEN + "Enter your choice (1-7): " + Style.RESET_ALL)
        
        if choice == '1':
            about_me()
        elif choice == '2':
            skills()
        elif choice == '3':
            projects()
        elif choice == '4':
            contact()
        elif choice == '5':
            ascii_art_generator()
        elif choice == '6':
            matrix_rain_effect()
        elif choice == '7':
            print_with_effect("Thank you for visiting. Goodbye!", color=Fore.RED)
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()
