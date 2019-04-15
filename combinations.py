drops_per_m3 = 2.0e7
m3_per_km3 = 1000 * 1000 * 1000
volume_ocean_km3 = 1_386_000_000
drops_per_km3 = drops_per_m3 * m3_per_km3
drops_in_ocean = volume_ocean_km3 * drops_per_km3

print('Drops in Ocean: %.03E' % drops_in_ocean)

step_meters = 1.0
earth_circumference_km = 40000
earth_circumference_m = earth_circumference_km * 1000
steps_around_earth = earth_circumference_m / step_meters
print('Steps around earth: %.03E' % steps_around_earth)

years_per_step = 1e12
circle_earth_years = steps_around_earth * years_per_step
print('Years to circle earth: %.03E' % circle_earth_years)

width_of_paper_mm = 0.1
papers_per_m = width_of_paper_mm * 1000
dist_to_pluto_m = 7_500_000_000_000
papers_to_pluto = papers_per_m * dist_to_pluto_m
print('Papers to pluto: %.03E' % papers_to_pluto)

secs_per_year = 365 * 24 * 60 * 60
print('Seconds per year: %.03E' % secs_per_year)

secs_per_circle = secs_per_year * circle_earth_years
secs_per_ocean = secs_per_circle * drops_in_ocean
secs_to_pluto = secs_per_ocean * papers_to_pluto
secs_to_space = secs_per_ocean * papers_per_m * 100_000

print(f'Secs to space: {secs_to_space:.03E}')
print(f'Years to space: {secs_to_space / secs_per_year:.03E}')

print(f'Secs to circle earth: {secs_per_circle:.03E}')
print(f'Years to empty ocean: {secs_per_ocean / secs_per_year:.03E}')
print(f'Secs to empty ocean: {secs_per_ocean:.03E}')
print(f'Years to pluto: {secs_to_pluto / secs_per_year:.03E}')
print(f'Secs to pluto: {secs_to_pluto:.03E}')

card_combos = 8.0658175e+67
divisor = card_combos / secs_to_pluto
print('Total combinations in 52!: %.03E' % card_combos)
print(f'How many times to 52!: {divisor:,.02f}')
