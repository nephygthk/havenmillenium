from django.urls import path

from . import views

app_name = 'transactions'

urlpatterns = [
    path("deposit/", views.DepositMoneyView.as_view(), name="deposit_money"),
    path("withdraw/", views.WithdrawMoneyView.as_view(), name="withdraw_money"),
    path("account/all_transactions/", views.TransactionListView.as_view(), name="all_transactions"),
    path("delete_transaction/<pk>/", views.delete_transaction, name="delete_transaction"),
    path("account/transfer/", views.CustomerWithdrawMoneyView.as_view(), name="customer_transfer"),
    path("account/international-transfer/", views.InternationalTransferView.as_view(), name="internation_transfer"),
    path("transaction_successful/", views.transaction_successful, name="transaction_successful"),
    path("transaction_failed/", views.transaction_failed, name="transaction_failed"),
    path("select_transafer_type/", views.select_transafer_type, name="select_transafer_type"),
    path("authorize-transaction/", views.verify_transaction_pin, name="verify_transaction_pin"),
]