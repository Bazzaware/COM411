def  cross_bridge(steps):
    for step in range(steps):
        print("Crossed step")

    if (step >= 5):
        print( "The bridge is collapsing!")
    else:
        print( "we must keep going!")


cross_bridge(3)
cross_bridge(6)
