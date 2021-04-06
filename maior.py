nums = list(range(5))
maior = 0

for i in nums:
	nums[i] = int(input("Digite um valor:"))
	if nums[i] > maior:
		maior = nums[i]
print(maior)