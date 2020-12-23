class SoldoutError(Exception):
    pass


chicken = 10
waiting = 1
while True:
    try:
        print("[남은 치킨: {0}마리]".format(chicken))
        order = int(input("치킨을 몇마리 주문하실 겁니까?"))
        if order <= 0 or type(order) != int:
            raise ValueError
        elif order > chicken:
            print("재료가 모자릅니다.")
        else:
            print("[{0}번째 대기손님] {1}마리 주문이 완료 되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldoutError
    except ValueError:
        print("주문이 완료 되지 못하였습니다.")

    except SoldoutError:
        print("재고 소진 주문 안받")
        break
