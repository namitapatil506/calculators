from django.urls import path
from . import views

urlpatterns = [

    path('fan-calculator/', views.fan_calculator, name='fan_calculator'),
    path('escapevelocity-calculator/', views.escapevelocity_calculator, name='escapevelocity_calculator'),
    path("elastic-potential-energy-calculator/", views.elastic_potential_energy_calculator,name="elastic_potential_energy_calculator"),
    path("simple-pendulum-calculator/", views.simple_pendulum_calculator,name="simple_pendulum_calculator"),
    path("specific-heat-calculator/", views.specific_heat_calculator,name="specific_heat_calculator"),
    path("thin-lens-equation-calculator/", views.thin_lens_equation_calculator,name="thin_lens_equation_calculator"),
    path("stokes-law-calculator/", views.stokes_law_calculator,name="stokes_law_calculator"),
    path("conservation-of-momentum-calculator/", views.conservation_of_momentum_calculator,name="conservation_of_momentum_calculator"),
    path("wet-bulb-calculator/", views.wet_bulb_calculator,name="wet_bulb_calculator"),
    path("electrical-power-calculator/", views.electrical_power_calculator,name="electrical_power_calculator"),
    path("joules-heating-calculator/", views.joules_heating_calculator,name="joules_heating_calculator"),
    path("poiseuille-law-calculator/", views.poiseuille_law_calculator,name="poiseuille_law_calculator"),
    path("wien-law-calculator/", views.wien_law_calculator,name="wien_law_calculator"),
    path("photon-energy-calculator/", views.photon_energy_calculator,name="photon_energy_calculator"),
    path("number-density-calculator/", views.number_density_calculator,name="number_density_calculator"),
    path("faraday-law-calculator/", views.faraday_law_calculator,name="faraday_law_calculator"),
    path("shockley-diode-calculator/", views.shockley_diode_calculator,name="shockley_diode_calculator"),
    path("photon-detection-efficiency-calculator/", views.photon_detection_efficiency_calculator,name="photon_detection_efficiency_calculator"),
    path("boltzmann-factor-calculator/", views.boltzmann_factor_calculator,name="boltzmann_factor_calculator"),
    path("dB-calculator/", views.dB_calculator,name="dB_calculator"),
    path("magnetic-force-between-wires-calculator/", views.magnetic_force_between_wires_calculator,name="magnetic_force_between_wires_calculator"),
    path("simple-harmonic-motion-calculator/", views.simple_harmonic_motion_calculator,name="simple_harmonic_motion_calculator"),
    path("solenoid-magnetic-field-calculator/", views.solenoid_magnetic_field_calculator,name="solenoid_magnetic_field_calculator"),
    path("solenoid-inductance-calculator/", views.solenoid_inductance_calculator,name="solenoid_inductance_calculator"),
    path("hydrogen-energy-levels-calculator/", views.hydrogen_energy_levels_calculator,name="hydrogen_energy_levels_calculator"),
    path("hydraulic-radius-calculator/", views.hydraulic_radius_calculator,name="hydraulic_radius_calculator"),
    path("parallel-capacitor-calculator/", views.parallel_capacitor_calculator,name="parallel_capacitor_calculator"),
    path("voltage-divider-calculator/", views.voltage_divider_calculator,name="voltage_divider_calculator"),
    path("acceleration-in-electric-field-calculator/", views.acceleration_in_electric_field_calculator,name="acceleration_in_electric_field_calculator"),
    path("magnetic-moment-calculator/", views.magnetic_moment_calculator,name="magnetic_moment_calculator"),
    path("parallel-resistor-calculator/", views.parallel_resistor_calculator,name="parallel_resistor_calculator"),
    path("projectile-motion-calculator/", views.projectile_motion_calculator,name="projectile_motion_calculator"),
    path("reverberation-time-calculator/", views.reverberation_time_calculator,name="reverberation_time_calculator"),
    path("doppler-effect-calculator/", views.doppler_effect_calculator,name="doppler_effect_calculator"),
    path("telescope-magnification-calculator/", views.telescope_magnification_calculator,name="telescope_magnification_calculator"),
    path("normal-force-calculator/", views.normal_force_calculator,name="normal_force_calculator"),
    path("hydraulic-jump-calculator/", views.hydraulic_jump_calculator,name="hydraulic_jump_calculator"),
    path("luminosity-calculator/", views.luminosity_calculator,name="luminosity_calculator"),
    path("hydraulic-pressure-calculator/", views.hydraulic_pressure_calculator,name="hydraulic_pressure_calculator"),
    path("acceleration-calculator/", views.acceleration_calculator,name="acceleration_calculator"),
    path("pulley-calculator/", views.pulley_calculator,name="pulley_calculator"),


]
