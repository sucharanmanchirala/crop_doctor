# Crop Doctor — Bug Fix Pass

## Fixed

1. **Heatmap dependency / duplicate implementation**
   - `main.py` no longer imports or uses `matplotlib` for heatmaps.
   - `crop_comparison.generate_difference_heatmap()` is now the single heatmap implementation.
   - Crop Raksha renders one heatmap image instead of maintaining two competing implementations.
   - `matplotlib` is still listed in `requirements.txt` as a deployment safety dependency.

2. **Translation wiring**
   - Added offline `translate_text()` support in `language.py` for the remaining major UI chrome and Crop Raksha status messages.
   - Added the Anjaneya navigation label to the language system.
   - Wired major Dashboard, Crop Registration, Crop Raksha, Diagnose, Monitoring, Disease Library, and About labels to the language system.
   - Crop Raksha chat now respects the selected English/Telugu/Hindi/Marathi language and resets its chat context when the language changes.
   - Existing disease content remains the original English source content; this avoids pretending an unverified machine translation is authoritative agricultural guidance.

3. **Diagnosis → registered crop linking**
   - General diagnosis can remain unlinked.
   - A diagnosis can now be explicitly linked to a registered crop.
   - Saved diagnosis records now include `crop_id`.
   - Anjaneya matches both new `crop_id` records and legacy diagnosis records that predate `crop_id` by crop name.

4. **Anjaneya integration**
   - `ivr/ivr_app.py` no longer calls `st.set_page_config()` when imported into `main.py`.
   - Added `render_anjaneya_voice()` for the single-app navigation flow.
   - The HTML/JS is rendered with fresh crop and history data each time the page is opened.
   - Added localized status/count labels and Marathi number-word recognition.
   - Updated branding to `Anjaneya — AI Voice Crop Guardian`.

5. **Monitoring day sequence**
   - `crop_raksha.py` now prefers stored observation day numbers, preventing same-day observations from producing duplicate day IDs.
   - Legacy records without a day field still have a backward-compatible fallback.

6. **Deployment compatibility**
   - Added `runtime.txt` with Python 3.11 to match the TensorFlow 2.17 environment used by the project.

## Validation

- All Python files compile successfully with `py_compile`.
- The embedded Anjaneya JavaScript passes `node --check`.
- The dependency-free Crop Raksha heatmap function was smoke-tested and returned a valid 224×224 PIL image.
