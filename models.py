# Create your models here.
from django.db import models



class wind_turbine(models.Model):

    # all modules register and login

    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    department= models.CharField(max_length=100, null=True)


    #user_id and mail password generation

    rh_id= models.CharField(max_length=100, null=True)
    password=models.PositiveBigIntegerField(null=True)



    # admin approve and reject

    approve = models.BooleanField(default=False)
    reject = models.BooleanField(default=False)

    # login and logout

    login = models.BooleanField(default=False)
    logout = models.BooleanField(default=False)



class blade(models.Model):

    # project_id........................................................

    project_id = models.CharField(max_length=100, null=True)

    # admin requirements and datas before ecryption.......................

    blade_length = models.CharField(max_length=100, null=True)
    blade_width = models.CharField(max_length=100, null=True)
    blade_weight = models.CharField(max_length=100, null=True)
    blade_circumference = models.CharField(max_length=100, null=True)
    

    # Module 1 - solvolysis

    # admin requirements and datas after ecryption

    encrypted_blade_length = models.CharField(max_length=100, null=True)
    encrypted_blade_width = models.CharField(max_length=100, null=True)
    encrypted_blade_weight = models.CharField(max_length=100, null=True)
    encrypted_blade_circumference = models.CharField(max_length=100, null=True)


    # encryption key

    solvo_decryption_key = models.CharField(max_length=64,null=True)

    # # get key and decrypt  

    solvo_get_key = models.BooleanField(default=False,null=True)
    solvo_decrypt = models.BooleanField(default=False,null=True)

    # admin requirements and datas after decryption

    decrypted_blade_length = models.CharField(max_length=100, null=True)
    decrypted_blade_width = models.CharField(max_length=100, null=True)
    decrypted_blade_weight = models.CharField(max_length=100, null=True)
    decrypted_blade_circumference = models.CharField(max_length=100, null=True)


    # solvo - Scanning

    measurement_of_cut_pieces = models.CharField(max_length=100,null=True)
    no_of_cut_pieces = models.CharField(max_length=100, null=True)
    methanolysis_heating_time = models.CharField(max_length=100, null=True)
    methanolysis_heating_temp = models.CharField(max_length=10, null=True)

    # Module 2 - reclamation ........................

    encrypted_measurement_of_cut_pieces = models.CharField(max_length=100, null=True)
    encrypted_no_of_cut_pieces = models.CharField(max_length=100, null=True)
    encrypted_methanolysis_heating_time = models.CharField(max_length=100, null=True)
    encrypted_methanolysis_heating_temp = models.CharField(max_length=100, null=True)

    # encryption key

    rec_decryption_key = models.CharField(max_length=64, null=True)

    # get key and decrypt

    rec_get_key = models.BooleanField(default=False, null=True)
    rec_decrypt = models.BooleanField(default=False, null=True)

    # decryption 

    decrypted_measurement_of_cut_pieces = models.CharField(max_length=100, null=True)
    decrypted_no_of_cut_pieces = models.CharField(max_length=100, null=True)
    decrypted_methanolysis_heating_time = models.CharField(max_length=100, null=True)
    decrypted_methanolysis_heating_temp = models.CharField(max_length=100, null=True)

    # rec - Scanning

    fibre_glass = models.CharField(max_length=100, null=True)
    carbon_fibre = models.CharField(max_length=100, null=True)
    balsa_wood = models.CharField(max_length=100, null=True)
    polyol = models.CharField(max_length=100, null=True)



    # Module - 3 - fabrication

    encrypted_fibre_glass = models.CharField(max_length=100, null=True)
    encrypted_carbon_fibre = models.CharField(max_length=100, null=True)
    encrypted_balsa_wood = models.CharField(max_length=100, null=True)
    encrypted_polyol = models.CharField(max_length=100, null=True)

    # encryption key

    fabric_decryption_key = models.CharField(max_length=64, null=True)

    # get key and decrypt

    fabric_get_key = models.BooleanField(default=False, null=True)
    fabric_decrypt = models.BooleanField(default=False, null=True)

    # decryption

    decrypted_fibre_glass = models.CharField(max_length=100, null=True)
    decrypted_carbon_fibre = models.CharField(max_length=100, null=True)
    decrypted_balsa_wood = models.CharField(max_length=100, null=True)
    decrypted_polyol = models.CharField(max_length=100, null=True)

    # dermato - Scanning

    c_carbon_fibre = models.CharField(max_length=100, null=True)
    f_fibre_glass = models.CharField(max_length=100, null=True)
    b_balsa_wood = models.CharField(max_length=100, null=True)
    pet_foam = models.CharField(max_length=100, null=True)
    flax_fibre = models.CharField(max_length=100, null=True)
    basalt_fibre = models.CharField(max_length=100, null=True)
    pecan_resin = models.CharField(max_length=100, null=True)



    # Module - 4 - ASSESSMENT

    

    encrypted_c_carbon_fibre = models.CharField(max_length=100, null=True)
    encrypted_f_fibre_glass = models.CharField(max_length=100, null=True)
    encrypted_b_balsa_wood = models.CharField(max_length=100, null=True)
    encrypted_pet_foam = models.CharField(max_length=100, null=True)
    encrypted_flax_fibre = models.CharField(max_length=100, null=True)
    encrypted_basalt_fibre = models.CharField(max_length=100, null=True)
    encrypted_pecan_resin = models.CharField(max_length=100, null=True)


    # encryption key

    assess_decryption_key = models.CharField(max_length=64, null=True)

    # get key and decrypt

    assess_get_key = models.BooleanField(default=False, null=True)
    assess_decrypt = models.BooleanField(default=False, null=True)


    # decryption

    decrypted_c_carbon_fibre = models.CharField(max_length=100, null=True)
    decrypted_f_fibre_glass = models.CharField(max_length=100, null=True)
    decrypted_b_balsa_wood = models.CharField(max_length=100, null=True)
    decrypted_pet_foam = models.CharField(max_length=100, null=True)
    decrypted_flax_fibre = models.CharField(max_length=100, null=True)
    decrypted_basalt_fibre = models.CharField(max_length=100, null=True)
    decrypted_pecan_resin = models.CharField(max_length=100, null=True)

    # assessment- Scanning

    static_testing = models.CharField(max_length=100, null=True)
    fatigue_testing = models.CharField(max_length=100, null=True)
    resonance_testing = models.CharField(max_length=100, null=True)
    environmental_testing = models.CharField(max_length=100, null=True)
    impact_testing = models.CharField(max_length=100, null=True)
    aerodynamic_testing = models.CharField(max_length=100, null=True)
    acoustic_testing = models.CharField(max_length=100, null=True)
    lightning_strike_testing = models.CharField(max_length=100, null=True)
    non_destructive_testing = models.CharField(max_length=100, null=True)
    full_scale_blade_testing = models.CharField(max_length=100, null=True)


    

    ### all modules scanned name

    solvo_scanned = models.BooleanField(default=False)
    rec_scanned =  models.BooleanField(default=False)
    fabric_scanned = models.BooleanField(default=False)
    assess_scanned = models.BooleanField(default=False)

    


    # all modules status

    status = models.CharField(default="Pending", null=True , max_length=100)

    # # reports

    report = models.BooleanField(default=False)
    rep = models.BooleanField(default=False)

    f_report = models.FileField(null=True, upload_to="Final_Report/")