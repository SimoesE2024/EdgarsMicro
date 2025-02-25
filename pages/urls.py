from django.urls import path
from .views import HomePageView, CreditoDiarioView, CreditoRelampagoView, CreditoPlusView, CreditoEmpresaView
from .views import signup

urlpatterns = [
    # Página inicial com class-based view
    path('', HomePageView.as_view(), name='home'),
    
    # Crédito Diário com class-based view
    path('credito_diario/', CreditoDiarioView.as_view(), name='credito_diario'),
    
    # Crédito Relâmpago com class-based view
    path('credito_relampago/', CreditoRelampagoView.as_view(), name='credito_relampago'),
    
    # Crédito Plus com class-based view
    path('credito_plus/', CreditoPlusView.as_view(), name='credito_plus'),
    
     # Crédito Empresa com class-based view
    path('credito_empresa/', CreditoEmpresaView.as_view(), name='credito_empresa'),
    
    # Signup com função de view
    path('signup/', signup, name='signup'),
]
