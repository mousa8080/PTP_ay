from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import User, Payment, Deposit
from .serializers import UserSerializer, PaymentSerializer, DepositSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PaymentViewSet(viewsets.ModelViewSet):  # ✅ ModelViewSet لعمليات الدفع
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        uid = request.data.get('uid')

        if not uid:
            return Response({'message': 'Missing_UID'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(uid=uid)
        except User.DoesNotExist:
            return Response({'message': 'Not_Registered'}, status=status.HTTP_404_NOT_FOUND)

        fare = 5.00
        if user.balance < fare:
            return Response({'message': 'Insufficient_Balance'}, status=status.HTTP_400_BAD_REQUEST)

        new_balance = user.balance - fare
        user.balance = new_balance
        user.save()

        payment = Payment.objects.create(user=user, fare=fare, new_balance=new_balance)
        return Response(PaymentSerializer(payment).data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        Payment.objects.all().delete()
        return Response({'message': 'All payments cleared'}, status=status.HTTP_200_OK)

class DepositViewSet(viewsets.ModelViewSet):  # ✅ ModelViewSet لعمليات الإيداع
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer

    def create(self, request, *args, **kwargs):
        uid = request.data.get('uid')
        amount = request.data.get('amount')
        deposit_method = request.data.get('deposit_method')

        if not uid or not amount or not deposit_method:
            return Response({'message': 'Invalid Data'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(uid=uid)
        except User.DoesNotExist:
            return Response({'message': 'Not_Registered'}, status=status.HTTP_404_NOT_FOUND)

        amount = float(amount)
        new_balance = user.balance + amount
        user.balance = new_balance
        user.save()

        deposit = Deposit.objects.create(user=user, amount=amount, new_balance=new_balance, deposit_method=deposit_method)
        return Response(DepositSerializer(deposit).data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        Deposit.objects.all().delete()
        return Response({'message': 'All deposit records cleared'}, status=status.HTTP_200_OK)
