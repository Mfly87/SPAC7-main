from dataClasses.dataTypes import Product, Category


prod = Product("abc","abc","abc","abc",123,123)
cat0 = Category("abc","abc","abc")
cat2 = Category("abc","abc","abc")
cat1 = Category("def","def","def")

print(cat0 == cat1)
print(cat2 == cat1)
print(cat0 == cat2)
print(cat0 == prod)

