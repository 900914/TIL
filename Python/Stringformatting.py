a = 40

print(f'this is {a}')

print('it is same as {}'.format(a))

print('also same as %d' % (a))

# unpack the list
#　変数の数が要素の数より少ない場合は、変数名に＊をつけると要素がリストとしてまとめて代入される
format_list = ['鶴','亀']
print('{}は1000年,{}は10000年'.format(*format_list))


# unpack sample
t = (0, 1, 2)
a, b, c = t
print(a)
print(b)
print(c)

print('my favorite actors are %(foo)s and %(bar)s.' % {'foo': '木村拓哉','bar': '松本潤'})

person = {'name':'Matsumoto','age':33}
sentence = 'Hello this is {0[name]} and I am {0[age]} years old.'.format(person)

print(sentence)

l = ['NINO','MIYA']
sentence = 'my name is {0[0]}{0[1]}'.format(l)

