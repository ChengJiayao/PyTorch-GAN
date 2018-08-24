

## For Jiayao [Friday Aug. 24 - week assignment]
1. Study InfoGAN code and play with it by changing parameters and datsets. 
2. Take celeb dataset and maximize one attribute MI (e.g., skin color (if there is any, or hair color))
2. * find a better dataset 
3. The goal for this week is to understand how to disentangle a feature from the data.
To check if the experiment is successful you'll need to :
	a. say z_i be the variable used to maximize MI between our protected attribute and its values
	b. Take an image (or better take a random vector of noise, vary only the z_i variable in its domain, while fixing the value of the other variables).
		- Do the output images show what you expect? I.e., changing the value for the attribute we had in mind.
		- If so, it means that we correctly learn to entangle the hair color attribute to the variable of reference.
	
	[c] To test the step above more systematically we can build a classifier which is trained to classify the value of the feature of interest. For instance, a classifier to identify if the colors are blond, black, or brown...
	Then use a batch of noise vector Z = {z^k}_{k=1}^n
	for each of this z^k select m points equipoised in z_i^k
	classify this new G(z^k) with our classifier. 
	For a given value for z_i^k, (for all k) is the classifier's output consistent? I.e., they all have blond hairs? 

	d. Now take an image G(z) produced by some noise vector z, and vary the attribute z_i.
		- Do you see changes in the other attributes z_j (j != i)?
		  For instance, if z_i represents hair color, and moving z_i makes also skin color change, 
		- If it does not than it means that our process did not correctly disentangle the semantic of hair color with the semantic of the other features of the image.

Note: If you have multiple attributes (i.e., different hair colors) you may need to try to use different latent variables. For instance, if you have 3 hair colors, you may use 3 latent variables (one associated to blond, one to black, one to brown).



## Notes on InfoGAN:
- Start with simple dataset (e.g., minst)
	- have architecture to generate input -> noise -> output
	- while minimizing MI for character boldness

- Select feature to protect (e.g., gender).
- Learn latent code for gender by minimizing MU of it.
- From input image, reconstruct latent code.
- Generate new image which is at least K \Delta far from the reconstructed latent code

- In the future we should also learn how to disentagnle this feature from all of the other features.




## Todo (Later Steps):
1. add cycle consistency 