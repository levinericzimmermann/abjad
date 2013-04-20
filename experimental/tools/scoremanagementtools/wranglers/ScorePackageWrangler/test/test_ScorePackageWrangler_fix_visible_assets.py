from experimental import *


def test_ScorePackageWrangler_fix_visible_assets_01():

    studio = scoremanagementtools.studio.ScoreManager()
    wrangler = studio.score_package_wrangler
    wrangler.session.show_all_scores()

    assert all(wrangler.fix_visible_assets(is_interactive=False))
