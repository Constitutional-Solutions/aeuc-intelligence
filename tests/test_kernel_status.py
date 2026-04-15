import pathlib

from core.family_kernel import check_kernel_status


def test_kernel_status_basics() -> None:
    """Smoke test for kernel status helper.

    This test assumes the repository layout used in development and verifies
    that the kernel status call does not raise and returns plausible fields.
    """

    repo_root = pathlib.Path(__file__).resolve().parents[1]
    status = check_kernel_status(repo_root)

    # Charter should either be verified or explicitly marked not-ok; in both
    # cases the field must be a boolean.
    assert isinstance(status.charter_ok, bool)

    # Sabbath status must be a boolean.
    assert isinstance(status.is_sabbath_now, bool)

    # Active member IDs should be a list of strings (may be empty in minimal setups).
    assert isinstance(status.active_member_ids, list)
    for mid in status.active_member_ids:
        assert isinstance(mid, str)
