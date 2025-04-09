# Initialize variables
has_license=True
has_space=True
has_experience=False

# Calculate conditions
can_sell_regular_pet = has_space and (has_license or has_experience )
can_sell_exotic_pet = has_space and has_license and has_experience
cannot_sell_any_pet = not( has_license and has_experience or has_space)

# Don't delete the lines below
print("Can sell regular pet:", can_sell_regular_pet)
print("Can sell exotic pet:", can_sell_exotic_pet)
print("Cannot sell any pet:", cannot_sell_any_pet)