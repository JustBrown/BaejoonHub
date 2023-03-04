nums = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'quarter', 'sixteen', 'seventeen', 'eighteen', 'nineteen',
        'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 
        'twenty six', 'twenty seven', 'twenty eight', 'twenty nine', 'half' ]

h = int(input())
m = int(input())

if m==0:
    print(nums[h], 'o\' clock')
elif m<=30:
    print(nums[m], 'past' if m==15 or m==30 else ('minute past' if m==1 else 'minutes past'), nums[h])
else:
    print(nums[60-m], 'to' if m==45 else ('minute to' if m==59 else 'minutes to'), nums[h+1 if h+1<=12 else 1])