from rest_framework import serializers
from .models import Flight, Passenger, Reservation

import re 
from datetime import date

# Custon validation function for  departure date

def validate_departure_date(value):

    if value<date.today():
        raise serializers.ValidationError('Departure date must be iin future.')
    return value


# Flight serializer with with custom validation

class FlightSerializer(serializers.ModelSerializer):
    dateOfDeparture = serializers.DateField(validators=[validate_departure_date])

    class Meta: 
        model = Flight
        fields= '__all__'

        def validate_phone(self, value):

            if len(value) != 10:
                raise serializers.ValidationError("Phone number should have exactly ten digits.")
            
            if not value.isdigit():
                raise serializers.ValidationError("Only numbers are allowed in phone field")
            
            return value
        

        def validate(self, data):
            """
            Object-level validation for the Passenger object.
            """
            # Check if the first name and last name are the same
            first_name = data.get('firstName')
            last_name = data.get('lastName')
            if first_name and last_name and first_name.lower() == last_name.lower():
             raise serializers.ValidationError("First name and last name cannot be the same.")
        
            return data
        

# --- Passenger Serializer ---
class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

    def validate_phone(self, value):
        """
        Field-level validation for the 'phone' field in the Passenger model.
        Here, we can add custom validation logic for the 'phone' field.
        """
        # Example: Ensure the phone number is exactly 10 digits long.
        if len(value) != 10:
            raise serializers.ValidationError("Phone number must be 10 digits long.")

        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only numeric digits.")
        
        return value
    
    def validate(self, data):
        """
        Object-level validation for the Passenger object.
        """
        # Check if the first name and last name are the same
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        if first_name and last_name and first_name.lower() == last_name.lower():
            raise serializers.ValidationError("First name and last name cannot be the same.")
        
        return data


# Reservation serializer 

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

        
