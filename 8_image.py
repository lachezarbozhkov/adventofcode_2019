import numpy as np

with open("8_image.txt", "r") as f:
    content = f.read().strip("\n")

array = np.reshape([int(i) for i in content], (-1, 6, 25))
print("Array shape:", array.shape)

max_zero = array.shape[1] * array.shape[2]
index = -1
for i in range(array.shape[0]):
    r = (array[i, :, :] == 0).sum()
    if r < max_zero:
        max_zero = r
        index = i

print(f"The layer containing least zeros is index {index} with {max_zero} zeros.")
print("On that layer, what is the number of 1 digits multiplied by the number of 2 digits?")
print((array[11,:,:] == 1).sum() * (array[11,:,:]==2).sum())



def get_image(array):
    new_array = np.zeros_like(array[1, :, :])
    for i in range(array.shape[1]):
        for j in range(array.shape[2]):
            digits = array[:, i, j]
            new_array[i, j] = [d for d in digits if d != 2][0]
    return new_array

demo_array = np.reshape([int(i) for i in "0222112222120000"], (-1, 2, 2))
demo_image = get_image(demo_array)
print("Demo image:")
print(demo_image)


image = get_image(array)
print("The image:")
print(image)