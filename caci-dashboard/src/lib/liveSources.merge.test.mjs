import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mergeLive } from './liveSources.js';

test('mergeLive overrides l/e/gdp when live present, keeps CSV otherwise', () => {
  const base = {
    USA: { f_total: 100, f: 100, e: 86.2, gdp: 31.9, l: 1.679, r: 1.0 },
    EU:  { f_total: 50,  f: 40,  e: 154.9, gdp: 18.0, l: 2.136, r: 1.0 },
  };
  const live = {
    workforce: { USA: 1.8, EU: 2.2 },
    energy:    { EU: 150.0 },
    gdp:       { USA: 30.0 },
  };
  const { merged, status } = mergeLive(base, live);
  assert.equal(merged.USA.l, 1.8);
  assert.equal(merged.EU.l, 2.2);
  assert.equal(merged.EU.e, 150.0);
  assert.equal(merged.USA.e, 86.2);
  assert.equal(merged.USA.gdp, 30.0);
  assert.equal(merged.EU.gdp, 18.0);
  assert.equal(merged.USA.f_total, 100);
  assert.equal(status.l, 'live');
  assert.equal(status.gdp, 'live');
  assert.equal(status.eUs, 'csv');
});

test('mergeLive with empty live keeps everything from CSV', () => {
  const base = { USA: { f_total: 100, f: 100, e: 86.2, gdp: 31.9, l: 1.679, r: 1.0 } };
  const { merged, status } = mergeLive(base, { workforce: {}, energy: {}, gdp: {} });
  assert.deepEqual(merged.USA, base.USA);
  assert.equal(status.l, 'csv');
  assert.equal(status.e, 'csv');
  assert.equal(status.gdp, 'csv');
});

test('mergeLive with no live arg degrades to all CSV', () => {
  const base = { USA: { f_total: 100, f: 100, e: 86.2, gdp: 31.9, l: 1.679, r: 1.0 } };
  const { merged, status } = mergeLive(base);
  assert.deepEqual(merged.USA, base.USA);
  assert.equal(status.l, 'csv');
  assert.equal(status.e, 'csv');
  assert.equal(status.gdp, 'csv');
  assert.equal(status.eUs, 'csv');
});
