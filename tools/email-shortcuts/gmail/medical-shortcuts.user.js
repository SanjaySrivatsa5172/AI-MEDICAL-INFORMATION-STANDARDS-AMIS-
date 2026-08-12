// ==UserScript==
// @name         Medical Procedure Shortcuts for Gmail
// @namespace    amis.medical.shortcuts
// @version      1.0.0
// @description  Ctrl+R/L/P/V/S insert vein-procedure phrases while typing in Gmail (compose body, subject, reply box)
// @match        https://mail.google.com/*
// @run-at       document-start
// @grant        none
// ==/UserScript==

// ============================================================================
// Install: add the Tampermonkey (or Violentmonkey) browser extension, create a
// new userscript, paste this whole file, save. Works on mail.google.com only,
// and only while the cursor is in an editable field - so Ctrl+V still pastes
// normally on every other website.
//
// NOTE: while typing in Gmail, these shortcuts REPLACE Ctrl+V paste,
// Ctrl+S save, Ctrl+P print and Ctrl+R refresh. To keep those, change
// REQUIRE_ALT below to true and use Ctrl+Alt+letter instead.
// ============================================================================

(function () {
  'use strict';

  // ========================== EDIT SNIPPETS HERE ============================
  const REQUIRE_ALT = false; // true = shortcuts become Ctrl+Alt+letter

  const SNIPPETS = {
    r: 'RIGHT GSV (AK) AND RIGHT GSV (BK) VARITHENA AND RIGHT LEG SCLEROTHERAPY',
    l: 'LEFT GSV (AK) RFA AND LEFT GSV (BK) VARITHENA AND LEFT LEG SCLEROTHERAPY',
    p: 'RIGHT/LEFT CALF PERFORATOR EVLT',
    v: 'VARITHENA OF LARGE VARICES RIGHT/LEFT LEG',
    s: 'SCLEROTHERAPY OF BILATERAL LEGS'
  };
  // ==========================================================================

  function modifiersMatch(e) {
    if (!e.ctrlKey || e.metaKey || e.shiftKey) return false;
    return REQUIRE_ALT ? e.altKey : !e.altKey;
  }

  function isEditable(el) {
    if (!el) return false;
    if (el.isContentEditable) return true; // Gmail compose / reply body
    const tag = el.tagName;
    if (tag === 'TEXTAREA') return true;
    return tag === 'INPUT' && /^(text|search|email)$/.test(el.type); // e.g. subject line
  }

  function insertText(el, text) {
    if (el.isContentEditable) {
      document.execCommand('insertText', false, text);
      return;
    }
    const start = el.selectionStart ?? el.value.length;
    const end = el.selectionEnd ?? el.value.length;
    el.setRangeText(text, start, end, 'end');
    el.dispatchEvent(new Event('input', { bubbles: true }));
  }

  document.addEventListener(
    'keydown',
    function (e) {
      if (!modifiersMatch(e)) return;
      const key = (e.key || '').toLowerCase();
      if (!Object.prototype.hasOwnProperty.call(SNIPPETS, key)) return;
      const target = document.activeElement;
      if (!isEditable(target)) return;
      e.preventDefault();
      e.stopImmediatePropagation(); // keep Gmail's own handlers out of the way
      insertText(target, SNIPPETS[key]);
    },
    true // capture phase, so this runs before Gmail's shortcut handling
  );
})();
