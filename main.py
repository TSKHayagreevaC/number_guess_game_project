# This File Is About Python And Scope

# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"Enemies Inside Function: {enemies}")

# increase_enemies()
# print(f"Enemies Outside Function: {enemies}")

# Local Scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength)

# Global Scope

# player_health = 10

# def drink_potion():
#     print(player_health)
#     potion_strength = 5
#     print(potion_strength)
# print(player_health)
# drink_potion()

# Modifying Global Scope

# enemies = "Skeleton"

# def increase_enemies():
#     enemies = "Zombies"
#     print(f"enemies inside fuction: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Modifying Numerical Variables

# enemies = 1

# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function : {enemies}")
# increase_enemies()
# print(f"enemies outside function : {enemies}")

# Global Constants

# PI = 3.14159
# URL = "https://www.google.com"
# TWITTER_HANDLE = "TSKHayagreevaC@twitter"
