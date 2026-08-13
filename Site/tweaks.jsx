/* Tweaks panel for Vocação redesign */
const { useEffect } = React;

function App() {
  const [t, setTweak] = useTweaks(window.__TWEAKS__ || {});

  useEffect(() => {
    if (window.__applyTweaks) window.__applyTweaks(t);
  }, [t]);

  return (
    <TweaksPanel title="Tweaks">
      <TweakSection label="Cor">
        <TweakColor
          label="Acento"
          value={t.accent}
          onChange={(v) => setTweak('accent', v)}
          options={['#C2410C', '#E5B910', '#2A6FDB', '#1F1F1F', '#A24A1B', '#7C3AED']}
        />
        <TweakRadio
          label="Paleta"
          value={t.palette}
          onChange={(v) => setTweak('palette', v)}
          options={[
            { value: 'warm', label: 'Warm' },
            { value: 'cool', label: 'Cool' },
            { value: 'mono', label: 'Mono' },
          ]}
        />
        <TweakToggle
          label="Granulação"
          value={t.grain !== false}
          onChange={(v) => setTweak('grain', v)}
        />
      </TweakSection>

      <TweakSection label="Tipografia">
        <TweakSelect
          label="Display"
          value={t.displayFont}
          onChange={(v) => setTweak('displayFont', v)}
          options={[
            'Poppins',
            'Fraunces',
            'Instrument Serif',
            'DM Serif Display',
            'Montserrat',
            'Geist',
          ]}
        />
        <TweakSelect
          label="Corpo"
          value={t.bodyFont}
          onChange={(v) => setTweak('bodyFont', v)}
          options={[
            'Geist',
            'DM Sans',
            'Manrope',
          ]}
        />
      </TweakSection>

      <TweakSection label="Ações">
        <TweakButton label="Re-tocar animações" onClick={() => {
          document.querySelectorAll('.reveal').forEach(el => {
            el.classList.remove('in');
            requestAnimationFrame(() => requestAnimationFrame(() => el.classList.add('in')));
          });
        }} />
        <TweakButton label="Voltar ao topo" secondary onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })} />
      </TweakSection>
    </TweaksPanel>
  );
}

ReactDOM.createRoot(document.getElementById('tweaks-root')).render(<App />);
