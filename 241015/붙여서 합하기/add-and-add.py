A, B = map(str, input().split())

AB, BA = A + B, B + A

print(int(AB) + int(BA))