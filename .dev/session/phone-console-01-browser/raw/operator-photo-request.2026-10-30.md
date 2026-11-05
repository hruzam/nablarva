# Operator addition — gallery and camera

Said: Majkee, 2026-10-30: “Can we add possibility to load photo from galery | mobile photoaparte.”

This is a requested addition to file input, not a canon change or permission to send
images automatically into a terminal. Terminal usability is still the first gate.

Candidate implementation within the existing file vault scope: separate Gallery
and Camera controls using native file inputs (image accept filter; camera capture
hint), show the selected image, explicit upload to the dedicated workstation vault,
then return an attachment path. No automatic prompt submission. The browser/Android
chooser determines camera availability; actual Firefox behaviour needs testing.
The operator has been asked whether workstation attachment or phone-only preview
is intended; no answer yet. No upload endpoint exists in the ttyd trial.

References checked: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file
and https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/capture .

## Operator clarification

Said: “Save to workstation and ask if can erase, allowing batch operations
(multiple selection).” Deletion target explicitly confirmed: “Phone originals
after verified upload.”

Required: multi-select gallery batch, camera capture, explicit upload with per-file
acknowledgement and content verification; only then ask about source deletion.
Normal browser-selected File objects grant read access, not authority/API to delete
the gallery originals. Browser-only delivery must offer a clear manual Gallery
cleanup handoff; automatic source deletion would need separately reviewed native
Android mediation and platform consent. Do not claim an erase button works from
the browser or silently substitute deleting workstation copies.
