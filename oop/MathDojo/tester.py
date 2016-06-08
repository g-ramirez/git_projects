from mathdojo import MathDojo

md = MathDojo()
print md.add(2).add(2,5).subtract(3,2).result
print
print md.add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result
