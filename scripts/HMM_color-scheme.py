from chimera import runCommand as rc

rc("colordef darktan #989885855858")

# Define commands
commands = [
    "color darktan #11:.A-Z",
    "color blue #11:.a,.d",
    "color red #11:.b,.e",
    "color cyan #11:.c,.f",
    "color yellow #11:.i-n",
    "color forest green #11:.g-h,.o-p",
    "color purple #11:.q",
    "color hot pink #11:.t",
    "color orange #11:.v,.r",
    "color dim gray #11:.s,.u"
]

# Join commands with "; " to create reset_color
reset_color = "; ".join(commands)

###
rc(reset_color)
rc("color black,rl")
