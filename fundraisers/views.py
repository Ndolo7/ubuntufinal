from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from decimal import Decimal
from .forms import FundraisersBasicDetailsForm, FundraisersPersonalDetailsForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Fundraiser

#@login_required

def create_fundraiser_basic(request):
    if request.method == 'POST':
        form = FundraisersBasicDetailsForm(request.POST)
        if form.is_valid():
            # Convert Decimal to float for session storage
            basic_details = form.cleaned_data
            basic_details['goal_amount'] = float(basic_details['goal_amount'])

            # Store basic details in session
            request.session['fundraiser_basic_details'] = basic_details
            messages.success(request, "Basic details submitted successfully!")

            # Redirect to the next step
            return redirect('create/personal')  # Replace with your actual URL name
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = FundraisersBasicDetailsForm()

    return render(request, 'create_fundraiser_basic.html', {'form': form})



def create_fundraiser_personal(request):
    # Add print statements or logging to help debug
    form = FundraisersPersonalDetailsForm()

    if request.method == 'POST':
        # Check if basic details are in session
        basic_details = request.session.get('fundraiser_basic_details')
        print("Basic details from session:", basic_details)
        
        if not basic_details:
            messages.warning(request, 'Please complete the basic details first.')
            return redirect('create/basic')  # Redirect to basic details page
            
        # Process personal details form
        form = FundraisersPersonalDetailsForm(request.POST)
        
        # Add form validation debugging
        if not form.is_valid():
            print("Form errors:", form.errors)
            return render(request, 'create_fundraiser_personal.html', {'form': form})
            

        if form.is_valid() and request.user.is_authenticated:
           
            
            try:
                # Create fundraiser
                fundraiser = form.save(commit=False)
                fundraiser.user = request.user
                
                # Set basic details from session
                fundraiser.title = basic_details['title']
                fundraiser.description = basic_details['description']
                fundraiser.goal_amount = Decimal(str(basic_details['goal_amount']))
                fundraiser.category = basic_details['category']
                
                # Set initial status
                fundraiser.is_active = False

                # Save fundraiser
                fundraiser.save()

                # Clear session data
                del request.session['fundraiser_basic_details']

                # Activate fundraiser
                fundraiser.is_active = True
                fundraiser.save()

                messages.success(request, 'Fundraiser created and activated successfully.')
                return redirect('submit_details')  # Ensure this matches your URL name exactly
            
            except Exception as e:
                print(f"Exception during fundraiser creation: {e}")
                messages.error(request, f'An error occurred: {str(e)}')
                form = FundraisersPersonalDetailsForm()
                return render(request, 'create_fundraiser_personal.html', {'form': form})
    
        else:
        # GET request - show personal details form
            form = FundraisersPersonalDetailsForm()
    return render(request, 'create_fundraiser_personal.html', {'form': form})

def fundraiser_success(request):
    # Retrieve the most recently created fundraiser for the current user
    latest_fundraiser = Fundraiser.objects.filter(user=request.user).order_by('-created_at').first()
    return render(request, 'fundraisers/success.html', {
        'fundraiser': latest_fundraiser
    })





