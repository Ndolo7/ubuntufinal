from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from decimal import Decimal
from .forms import FundraisersBasicDetailsForm, FundraisersPersonalDetailsForm

from .models import Fundraiser

@login_required
def create_fundraiser_basic(request):
    if request.method == 'POST':
        form = FundraisersBasicDetailsForm(request.POST)
        if form.is_valid():
            # Convert Decimal to float for session storage
            basic_details = form.cleaned_data#.copy()
            basic_details['goal_amount'] = float(basic_details['goal_amount'])

            # Store basic details in session
            request.session['fundraiser_basic_details'] = basic_details
            return render(request, 'create_fundraiser_personal.html')
        else:
            form = FundraisersBasicDetailsForm()
    else:
        form = FundraisersBasicDetailsForm()

   # return render(request, 'fundraisers/create_fundraiser_basic.html', {'form': form})

@login_required
def create_fundraiser_personal(request):
    if FundraisersBasicDetailsForm not in request.session:
        messages.warning(request, 'Please complete the basic details first.')
        return redirect('create_fundraiser_basic')
    

    if request.method == 'POST':
        form = FundraisersPersonalDetailsForm(request.POST)
        if form.is_valid():
            # Retrieve basic details from session
            basic_details = request.session.get('fundraiser_basic_details')

            # Create fundraiser
            fundraiser = form.save(commit=False)
            fundraiser.user = request.user
            fundraiser.title = basic_details['title']
            fundraiser.description = basic_details['description']

            # Convert back to Decimal
            fundraiser.goal_amount = Decimal(str(basic_details['goal_amount']))
            fundraiser.category = basic_details['category']
            fundraiser.is_active = False  # Default to inactive

            fundraiser.save()

            # Clear session data
            del request.session['fundraiser_basic_details']

            # Add success message
            messages.success(request, 'Fundraiser created and pending approval.')

            # Redirect to success page
            return redirect('fundraisers:submit_details')
   # else:
  #      form = FundraiserPersonalDetailsForm()

    return render(request, 'fundraisers/create_fundraiser_personal.html', {'form': form})

@login_required
def activate_fundraiser(request, fundraiser_id):
    try:
        fundraiser = Fundraiser.objects.get(id=fundraiser_id, user=request.user)

        # Only allow activation if the fundraiser is not already active
        if not fundraiser.is_active:
            # TODO: Add additional checks like email verification, admin review, etc.
            fundraiser.is_active = True
            fundraiser.save()
            messages.success(request, 'Fundraiser has been activated.')
        else:
            messages.info(request, 'Fundraiser is already active.')

        return redirect('fundraiser_list')
    except Fundraiser.DoesNotExist:
        messages.error(request, 'Fundraiser not found.')
        return redirect('fundraiser_list')

@login_required
def fundraiser_success(request):
    # Retrieve the most recently created fundraiser for the current user
    latest_fundraiser = Fundraiser.objects.filter(user=request.user).order_by('-created_at').first()
    return render(request, 'fundraisers/success.html', {
        'fundraiser': latest_fundraiser
    })





