#Write a function that computes the volume of a sphere given its radius.
def volume_sphere(rad):
    volume=4*3.14*rad*rad*rad/3
    print(volume)
volume_sphere(int(input()))