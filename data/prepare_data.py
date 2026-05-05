import pandas as pd

# TESS
tess = pd.read_csv('data/prepared_exoplanets.csv')
tess['name'] = tess['toi'].apply(lambda x: f"TOI-{x}")
tess['source'] = 'TESS'
tess_clean = tess[['name', 'pl_rade', 'pl_orbper', 'pl_trandurh', 'source']].rename(columns={
    'pl_rade': 'radius',
    'pl_orbper': 'period',
    'pl_trandurh': 'duration'
})

# Kepler
kepler = pd.read_csv('data/kepler.csv', comment='#')
kepler['name'] = kepler.apply(
    lambda r: r['kepler_name'] if pd.notna(r['kepler_name']) else r['kepoi_name'], axis=1
)
kepler['source'] = 'Kepler'
kepler_clean = kepler[['name', 'koi_prad', 'koi_period', 'koi_duration', 'source']].rename(columns={
    'koi_prad': 'radius',
    'koi_period': 'period',
    'koi_duration': 'duration'
})

# Fusion
combined = pd.concat([tess_clean, kepler_clean], ignore_index=True)
combined = combined.dropna(subset=['radius', 'period', 'duration'])
combined = combined.drop_duplicates(subset=['name'])

print(f"Total: {len(combined)} exoplanètes")
print(combined.head(5))

combined.to_csv('data/combined_exoplanets.csv', index=False)
print("Saved to data/combined_exoplanets.csv")