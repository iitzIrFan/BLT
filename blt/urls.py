# Move social account imports to top
from allauth.socialaccount.providers.facebook import views as facebook_views
from allauth.socialaccount.providers.github import views as github_views
from allauth.socialaccount.providers.google import views as google_views
from captcha.views import captcha_refresh
from dj_rest_auth.registration.views import SocialAccountListView
from dj_rest_auth.views import PasswordResetConfirmView
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

import comments.views
from website.api.views import (
    ActivityLogViewSet,
    AuthApiViewset,
    BugHuntApiViewset,
    BugHuntApiViewsetV2,
    DomainViewSet,
    FlagIssueApiView,
    InviteFriendApiViewset,
    IssueViewSet,
    LeaderboardApiViewSet,
    LikeIssueApiView,
    OrganizationViewSet,
    ProjectViewSet,
    StatsApiViewset,
    TagApiViewset,
    TimeLogViewSet,
    UrlCheckApiViewset,
    UserIssueViewSet,
    UserProfileViewSet,
)
from website.views.bitcoin import (
    BaconSubmissionView,
    bacon_requests_view,
    bacon_view,
    batch_send_bacon_tokens_view,
    get_wallet_balance,
    initiate_transaction,
    pending_transactions_view,
    update_submission_status,
)
from website.views.blog import PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView
from website.views.company import (
    AddDomainView,
    AddHuntView,
    AddSlackIntegrationView,
    DomainView,
    EndBughuntView,
    Organization_view,
    OrganizationDashboardAnalyticsView,
    OrganizationDashboardIntegrations,
    OrganizationDashboardManageBughuntView,
    OrganizationDashboardManageBugsView,
    OrganizationDashboardManageDomainsView,
    OrganizationDashboardManageRolesView,
    OrganizationDashboardTeamOverviewView,
    RegisterOrganizationView,
    ShowBughuntView,
    SlackCallbackView,
    accept_bug,
    delete_manager,
    delete_prize,
    edit_prize,
)
from website.views.core import (
    CustomSocialAccountDisconnectView,
    FacebookConnect,
    FacebookLogin,
    GithubConnect,
    GithubLogin,
    GoogleConnect,
    GoogleLogin,
    MapView,
    RoadmapView,
    StatsDetailView,
    UploadCreate,
    add_forum_comment,
    add_forum_post,
    badge_list,
    check_owasp_compliance,
    donate_view,
    facebook_callback,
    features_view,
    find_key,
    github_callback,
    google_callback,
    home,
    management_commands,
    robots_txt,
    run_management_command,
    search,
    set_vote_status,
    sitemap,
    sponsor_view,
    stats_dashboard,
    status_page,
    submit_roadmap_pr,
    sync_github_projects,
    template_list,
    test_sentry,
    view_forum,
    view_pr_analysis,
    vote_forum_post,
    website_stats,
)
from website.views.domain import check_domain_security
from website.views.education import (
    add_lecture,
    add_section,
    course_content_management,
    create_or_update_course,
    create_standalone_lecture,
    delete_lecture,
    delete_section,
    edit_course,
    edit_lecture,
    edit_section,
    edit_standalone_lecture,
    education_home,
    enroll,
    get_course_content,
    get_lecture_data,
    get_section_data,
    instructor_dashboard,
    mark_lecture_complete,
    study_course,
    update_lectures_order,
    update_sections_order,
    view_course,
    view_lecture,
)
from website.views.issue import (
    AllIssuesView,
    ContributeView,
    GitHubIssueDetailView,
    GitHubIssuesView,
    GithubIssueView,
    IssueCreate,
    IssueEdit,
    IssueView,
    SaveBiddingData,
    SpecificIssuesView,
    UpdateIssue,
    change_bid_status,
    comment_on_content,
    create_github_issue,
    delete_content_comment,
    delete_issue,
    dislike_issue,
    fetch_current_bid,
    flag_issue,
    generate_bid_image,
    get_github_issue,
    get_unique_issues,
    issue_count,
    like_issue,
    newhome,
    page_vote,
    remove_user_from_issue,
    resolve,
    save_issue,
    search_issues,
    select_bid,
    submit_bug,
    submit_pr,
    unsave_issue,
    update_content_comment,
    vote_count,
)
from website.views.organization import (
    CreateHunt,
    DomainDetailView,
    DomainList,
    DomainListView,
    DraftHunts,
    HuntCreate,
    InboundParseWebhookView,
    Joinorganization,
    Listbounties,
    OngoingHunts,
    OrganizationDetailView,
    OrganizationListView,
    OrganizationSettings,
    PreviousHunts,
    ReportedIpListView,
    ReportIpView,
    RoomCreateView,
    RoomsListView,
    ScoreboardView,
    TimeLogListAPIView,
    TimeLogListView,
    UpcomingHunts,
    add_domain_to_organization,
    add_or_update_domain,
    add_or_update_organization,
    add_role,
    add_sizzle_checkIN,
    admin_organization_dashboard,
    admin_organization_dashboard_detail,
    approve_activity,
    checkIN,
    checkIN_detail,
    delete_room,
    delete_time_entry,
    dislike_activity,
    feed,
    get_scoreboard,
    hunt_results,
    join_room,
    like_activity,
    load_more_issues,
    organization_dashboard,
    organization_dashboard_domain_detail,
    organization_dashboard_hunt_detail,
    organization_dashboard_hunt_edit,
    organization_hunt_results,
    room_messages_api,
    send_message_api,
    sizzle,
    sizzle_daily_log,
    sizzle_docs,
    subscribe_to_domains,
    trademark_detailview,
    trademark_search,
    update_organization_repos,
    update_role,
    user_sizzle_report,
    view_hunt,
    weekly_report,
)
from website.views.ossh import (
    get_github_data,
    get_recommended_articles,
    get_recommended_communities,
    get_recommended_discussion_channels,
    get_recommended_repos,
    ossh_home,
    ossh_results,
)
from website.views.project import (
    ProjectBadgeView,
    ProjectsDetailView,
    ProjectView,
    RepoBadgeView,
    RepoDetailView,
    blt_tomato,
    create_project,
    distribute_bacon,
    select_contribution,
)
from website.views.queue import queue_list
from website.views.repo import RepoListView, add_repo
from website.views.slack_handlers import slack_commands, slack_events
from website.views.teams import (
    TeamChallenges,
    TeamLeaderboard,
    TeamOverview,
    add_member,
    create_team,
    delete_team,
    give_kudos,
    join_requests,
    kick_member,
    leave_team,
    search_users,
)
from website.views.user import (
    CustomObtainAuthToken,
    EachmonthLeaderboardView,
    GlobalLeaderboardView,
    InviteCreate,
    SpecificMonthLeaderboardView,
    UserChallengeListView,
    UserDeleteView,
    UserProfileDetailsView,
    UserProfileDetailView,
    assign_badge,
    badge_user_list,
    contributors,
    contributors_view,
    create_wallet,
    deletions,
    follow_user,
    get_score,
    github_webhook,
    invite_friend,
    profile,
    profile_edit,
    referral_signup,
    update_bch_address,
    user_dashboard,
    users_view,
)

admin.autodiscover()

# Use the drf_yasg schema view
schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

favicon_view = RedirectView.as_view(url="/static/favicon.ico", permanent=True)

router = routers.DefaultRouter()
router.register(r"issues", IssueViewSet, basename="issues")
router.register(r"userissues", UserIssueViewSet, basename="userissues")
router.register(r"profile", UserProfileViewSet, basename="profile")
router.register(r"domain", DomainViewSet, basename="domain")
router.register(r"timelogs", TimeLogViewSet, basename="timelogs")
router.register(r"activitylogs", ActivityLogViewSet, basename="activitylogs")

handler404 = "website.views.core.handler404"
handler500 = "website.views.core.handler500"

urlpatterns = [
    path("500/", TemplateView.as_view(template_name="500.html"), name="500"),
    path("", home, name="home"),
    path(
        "api/v1/organizations/",
        OrganizationViewSet.as_view({"get": "list", "post": "create"}),
        name="organization",
    ),
    path("invite-friend/", invite_friend, name="invite_friend"),
    path("referral/", referral_signup, name="referral_signup"),
    path("captcha/refresh/", captcha_refresh, name="captcha-refresh-debug"),
    path("captcha/", include("captcha.urls")),
    re_path(r"^auth/registration/", include("dj_rest_auth.registration.urls")),
    path(
        "rest-auth/password/reset/confirm/<str:uidb64>/<str:token>",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    re_path(r"^auth/", include("dj_rest_auth.urls")),
    re_path("auth/facebook", FacebookLogin.as_view(), name="facebook_login"),
    path("accounts/", include("allauth.urls")),
    path("accounts/delete/", UserDeleteView.as_view(), name="user_deletion"),
    path("auth/github/", GithubLogin.as_view(), name="github_login"),
    path("accounts/github/login/callback/", github_callback, name="github_callback"),
    re_path(r"^auth/github/connect/$", GithubConnect.as_view(), name="github_connect"),
    path("auth/github/url/", github_views.oauth2_login),
    path("auth/google/", GoogleLogin.as_view(), name="google_login"),
    path("accounts/google/login/callback/", google_callback, name="google_callback"),
    path("accounts/facebook/login/callback/", facebook_callback, name="facebook_callback"),
    re_path(r"^auth/facebook/connect/$", FacebookConnect.as_view(), name="facebook_connect"),
    re_path(r"^auth/google/connect/$", GoogleConnect.as_view(), name="google_connect"),
    path("auth/github/url/", github_views.oauth2_login),
    path(
        "oauth/slack/callback/",
        SlackCallbackView.as_view(),
        name="slack_oauth_callback",
    ),
    path("slack/commands/", slack_commands, name="slack_commands"),
    path("auth/google/url/", google_views.oauth2_login),
    path("auth/facebook/url/", facebook_views.oauth2_callback),
    path("socialaccounts/", SocialAccountListView.as_view(), name="social_account_list"),
    path(
        "add_domain_to_organization/",
        add_domain_to_organization,
        name="add_domain_to_organization",
    ),
    path(
        "socialaccounts/<int:pk>/disconnect/",
        CustomSocialAccountDisconnectView.as_view(),
        name="social_account_disconnect",
    ),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    re_path(r"^issues/$", newhome, name="issues"),
    re_path(
        r"^dashboard/organization/$",
        organization_dashboard,
        name="organization_dashboard_home",
    ),
    re_path(
        r"^dashboard/admin/organization$",
        admin_organization_dashboard,
        name="admin_organization_dashboard",
    ),
    re_path(
        r"^dashboard/admin/organization/addorupdate$",
        add_or_update_organization,
        name="add_or_update_organization",
    ),
    re_path(
        r"^dashboard/organization/domain/addorupdate$",
        add_or_update_domain,
        name="add_or_update_domain",
    ),
    path(
        "dashboard/organization/domain/<int:pk>/",
        organization_dashboard_domain_detail,
        name="organization_dashboard_domain_detail",
    ),
    path(
        "dashboard/organization/hunt/<int:pk>/",
        organization_dashboard_hunt_detail,
        name="organization_dashboard_hunt_detail",
    ),
    path("dashboard/user/hunt/<int:pk>/", view_hunt, name="view_hunt"),
    path(
        "dashboard/user/hunt/<int:pk>/submittion/",
        submit_bug,
        name="submit_bug",
    ),
    path(
        "dashboard/user/hunt/<int:pk>/results/",
        hunt_results,
        name="hunt_results",
    ),
    path(
        "dashboard/organization/hunt/<int:pk>/edit",
        organization_dashboard_hunt_edit,
        name="organization_dashboard_hunt_edit",
    ),
    path(
        "dashboard/admin/organization/<int:pk>/",
        admin_organization_dashboard_detail,
        name="admin_organization_dashboard_detail",
    ),
    re_path(
        r"^dashboard/organization/hunt/create$",
        CreateHunt.as_view(),
        name="create_hunt",
    ),
    path("hunt/<int:pk>", ShowBughuntView.as_view(), name="show_bughunt"),
    re_path(
        r"^dashboard/organization/hunt/drafts$",
        DraftHunts.as_view(),
        name="draft_hunts",
    ),
    re_path(
        r"^dashboard/organization/hunt/upcoming$",
        UpcomingHunts.as_view(),
        name="upcoming_hunts",
    ),
    re_path(
        r"^dashboard/organization/hunt/previous$",
        PreviousHunts.as_view(),
        name="previous_hunts",
    ),
    path(
        "dashboard/organization/hunt/previous/<int:pk>/",
        organization_hunt_results,
        name="organization_hunt_results",
    ),
    re_path(
        r"^dashboard/organization/hunt/ongoing$",
        OngoingHunts.as_view(),
        name="ongoing_hunts",
    ),
    re_path(r"^dashboard/organization/domains$", DomainList.as_view(), name="domain_list"),
    re_path(
        r"^dashboard/organization/settings$",
        OrganizationSettings.as_view(),
        name="organization-settings",
    ),
    re_path(r"^join$", Joinorganization.as_view(), name="join"),
    re_path(
        r"^dashboard/organization/settings/role/update$",
        update_role,
        name="update-role",
    ),
    re_path(
        r"^dashboard/organization/settings/role/add$",
        add_role,
        name="add-role",
    ),
    re_path(r"^dashboard/user/$", user_dashboard, name="user"),
    re_path(
        r"^dashboard/user/profile/(?P<slug>[^/]+)/$",
        UserProfileDetailsView.as_view(),
        name="user_profile",
    ),
    path(settings.ADMIN_URL + "/", admin.site.urls),
    re_path(r"^like_issue/(?P<issue_pk>\d+)/$", like_issue, name="like_issue"),
    re_path(
        r"^dislike_issue/(?P<issue_pk>\d+)/$",
        dislike_issue,
        name="dislike_issue",
    ),
    re_path(r"^flag_issue/(?P<issue_pk>\d+)/$", flag_issue, name="flag_issue"),
    re_path(r"^resolve/(?P<id>\w+)/$", resolve, name="resolve"),
    re_path(
        r"^create_github_issue/(?P<id>\w+)/$",
        create_github_issue,
        name="create_github_issue",
    ),
    re_path(r"^vote_count/(?P<issue_pk>\d+)/$", vote_count, name="vote_count"),
    path("domain/<int:pk>/subscribe/", subscribe_to_domains, name="subscribe_to_domains"),
    re_path(r"^save_issue/(?P<issue_pk>\d+)/$", save_issue, name="save_issue"),
    path("domain/<int:pk>/subscribe/", subscribe_to_domains, name="subscribe_to_domains"),
    re_path(r"^save_issue/(?P<issue_pk>\d+)/$", save_issue, name="save_issue"),
    path("domain/<int:pk>/subscribe/", subscribe_to_domains, name="subscribe_to_domains"),
    re_path(r"^save_issue/(?P<issue_pk>\d+)/$", save_issue, name="save_issue"),
    path("profile/edit/", profile_edit, name="profile_edit"),
    re_path(
        r"^unsave_issue/(?P<issue_pk>\d+)/$",
        unsave_issue,
        name="unsave_issue",
    ),
    re_path(r"^issue/edit/$", IssueEdit, name="edit_issue"),
    re_path(r"^issue/update/$", UpdateIssue, name="update_issue"),
    # comment on content
    path(
        "content/<str:content_pk>/comment/",
        comment_on_content,
        name="comment_on_content",
    ),
    # update comment
    path(
        "content/<str:content_pk>/comment/update/<str:comment_pk>/",
        update_content_comment,
        name="update_content_comment",
    ),
    # delete comment
    path("content/comment/delete/", delete_content_comment, name="delete_content_comment"),
    re_path(r"^issue/(?P<slug>\w+)/$", IssueView.as_view(), name="issue_view"),
    re_path(r"^follow/(?P<user>[^/]+)/", follow_user, name="follow_user"),
    re_path(r"^all_activity/$", AllIssuesView.as_view(), name="all_activity"),
    re_path(r"^label_activity/$", SpecificIssuesView.as_view(), name="all_activitys"),
    re_path(r"^leaderboard/$", GlobalLeaderboardView.as_view(), name="leaderboard_global"),
    re_path(
        r"^leaderboard/monthly/$",
        SpecificMonthLeaderboardView.as_view(),
        name="leaderboard_specific_month",
    ),
    re_path(
        r"^leaderboard/each-month/$",
        EachmonthLeaderboardView.as_view(),
        name="leaderboard_eachmonth",
    ),
    re_path(
        r"^api/v1/issue/like/(?P<id>\w+)/$",
        LikeIssueApiView.as_view(),
        name="api_like_issue",
    ),
    re_path(
        r"^api/v1/issue/flag/(?P<id>\w+)/$",
        FlagIssueApiView.as_view(),
        name="api_flag_issue",
    ),
    re_path(r"^api/v1/leaderboard/$", LeaderboardApiViewSet.as_view(), name="leaderboard"),
    re_path(
        r"^api/v1/invite_friend/",
        InviteFriendApiViewset.as_view(),
        name="api_invite_friend",
    ),
    path("scoreboard/", ScoreboardView.as_view(), name="scoreboard"),
    re_path(r"^issue/$", IssueCreate.as_view(), name="issue"),
    # link to index.html
    re_path(r"^index/$", TemplateView.as_view(template_name="index.html"), name="index"),
    re_path(
        r"^upload/(?P<time>[^/]+)/(?P<hash>[^/]+)/",
        UploadCreate.as_view(),
        name="upload",
    ),
    re_path(r"^profile/(?P<slug>[^/]+)/$", UserProfileDetailView.as_view(), name="profile"),
    re_path(r"^domain/(?P<slug>.+)/$", DomainDetailView.as_view(), name="domain"),
    re_path(
        r"^.well-known/acme-challenge/(?P<token>[^/]+)/$",
        find_key,
        name="find_key",
    ),
    re_path(r"^accounts/profile/", profile, name="account_profile"),
    path("delete_issue/<str:id>/", ensure_csrf_cookie(delete_issue), name="delete_issue"),
    re_path(
        r"^remove_user_from_issue/(?P<id>\w+)/$",
        remove_user_from_issue,
        name="remove_user_from_issue",
    ),
    re_path(r"^accounts/", include("allauth.urls")),
    re_path(
        r"^sitemap/$",
        sitemap,
        name="sitemap",
    ),
    re_path(
        r"^badges/$",
        badge_list,
        name="badges",
    ),
    re_path(
        r"^badges/(?P<badge_id>\d+)/users/$",
        badge_user_list,
        name="badge_user_list",
    ),
    re_path(r"^start/$", TemplateView.as_view(template_name="hunt.html"), name="start_hunt"),
    re_path(r"^hunt/$", login_required(HuntCreate.as_view()), name="hunt"),
    re_path(r"^bounties/$", Listbounties.as_view(), name="hunts"),
    path("api/load-more-issues/", load_more_issues, name="load_more_issues"),
    re_path(r"^invite/$", InviteCreate.as_view(template_name="invite.html"), name="invite"),
    re_path(r"^terms/$", TemplateView.as_view(template_name="terms.html"), name="terms"),
    re_path(r"^about/$", TemplateView.as_view(template_name="about.html"), name="about"),
    re_path(r"^teams/$", TemplateView.as_view(template_name="teams.html"), name="teams"),
    re_path(
        r"^googleplayapp/$",
        TemplateView.as_view(template_name="coming_soon.html"),
        name="googleplayapp",
    ),
    re_path(r"^projects/$", ProjectView.as_view(), name="project_list"),
    re_path(r"^apps/$", TemplateView.as_view(template_name="apps.html"), name="apps"),
    re_path(
        r"^deletions/$",
        deletions,
        name="deletions",
    ),
    re_path(r"^bacon/$", bacon_view, name="bacon"),
    re_path(r"^education/$", education_home, name="education"),
    path("education/instructor_dashboard/", instructor_dashboard, name="instructor_dashboard"),
    path("education/create-standalone-lecture/", create_standalone_lecture, name="create_standalone_lecture"),
    path("education/edit-standalone-lecture/<int:lecture_id>", edit_standalone_lecture, name="edit_standalone_lecture"),
    path("education/instructor_dashboard/edit-course/<int:course_id>/", edit_course, name="edit_course"),
    path(
        "education/instructor_dashboard/create-or-update-course/",
        create_or_update_course,
        name="create_or_update_course",
    ),
    path("education/view-course/<int:course_id>/", view_course, name="view_course"),
    path("education/view-lecture/<int:lecture_id>/", view_lecture, name="view_lecture"),
    path("education/enroll/<int:course_id>/", enroll, name="enroll"),
    path("education/study_course/<int:course_id>/", study_course, name="study_course"),
    path("education/mark-lecture-complete/", mark_lecture_complete, name="mark_lecture_complete"),
    path("education/get-course-content/<int:course_id>/", get_course_content, name="get_course_content"),
    path(
        "education/course-content-management/<int:course_id>/",
        course_content_management,
        name="course_content_management",
    ),
    path("education/instructor_dashboard/courses/<int:course_id>/sections/add/", add_section, name="add_section"),
    path("education/instructor_dashboard/sections/<int:section_id>/edit/", edit_section, name="edit_section"),
    path("education/instructor_dashboard/sections/<int:section_id>/delete/", delete_section, name="delete_section"),
    # Lecture management
    path("education/instructor_dashboard/sections/<int:section_id>/lectures/add/", add_lecture, name="add_lecture"),
    path("education/instructor_dashboard/lectures/<int:lecture_id>/edit/", edit_lecture, name="edit_lecture"),
    path("education/instructor_dashboard/lectures/<int:lecture_id>/delete/", delete_lecture, name="delete_lecture"),
    # API endpoints
    path("education/instructor_dashboard/api/lectures/<int:lecture_id>/", get_lecture_data, name="get_lecture_data"),
    path("education/instructor_dashboard/api/sections/<int:section_id>/", get_section_data, name="get_section_data"),
    path(
        "education/instructor_dashboard/courses/<int:course_id>/sections/reorder/",
        update_sections_order,
        name="update_sections_order",
    ),
    path(
        "education/instructor_dashboard/sections/<int:section_id>/lectures/reorder/",
        update_lectures_order,
        name="update_lectures_order",
    ),
    re_path(r"^gsoc/$", TemplateView.as_view(template_name="gsoc.html"), name="gsoc"),
    re_path(
        r"^privacypolicy/$",
        TemplateView.as_view(template_name="privacy.html"),
        name="privacy",
    ),
    re_path(r"^stats/$", StatsDetailView.as_view(), name="stats"),
    re_path(r"^favicon\.ico$", favicon_view),
    re_path(
        r"^sendgrid_webhook/$",
        csrf_exempt(InboundParseWebhookView.as_view()),
        name="inbound_event_webhook_callback",
    ),
    re_path(r"^status_page/$", status_page, name="status_page"),
    re_path(r"^status/run-command/$", run_management_command, name="run_management_command"),
    re_path(r"^status/commands/$", management_commands, name="management_commands"),
    path(r"website_stats/", website_stats, name="website_stats"),
    re_path(r"^issue/comment/add/$", comments.views.add_comment, name="add_comment"),
    re_path(r"^issue/comment/delete/$", comments.views.delete_comment, name="delete_comment"),
    re_path(r"^comment/autocomplete/$", comments.views.autocomplete, name="autocomplete"),
    re_path(
        r"^issue/(?P<pk>\d+)/comment/edit/$",
        comments.views.edit_comment,
        name="edit_comment",
    ),
    re_path(
        r"^issue/(?P<pk>\d+)/comment/reply/$",
        comments.views.reply_comment,
        name="reply_comment",
    ),
    re_path(r"^social/$", TemplateView.as_view(template_name="social.html"), name="social"),
    re_path(r"^search/$", search, name="search"),
    re_path(r"^report/$", IssueCreate.as_view(), name="report"),
    re_path(r"^i18n/", include("django.conf.urls.i18n")),
    re_path(r"^api/v1/", include(router.urls)),
    re_path(r"^api/v1/stats/$", StatsApiViewset.as_view(), name="get_score"),
    re_path(r"^api/v1/urlcheck/$", UrlCheckApiViewset.as_view(), name="url_check"),
    re_path(r"^api/v1/hunt/$", BugHuntApiViewset.as_view(), name="hunt_details"),
    re_path(r"^api/v2/hunts/$", BugHuntApiViewsetV2.as_view(), name="hunts_detail_v2"),
    re_path(r"^api/v1/userscore/$", get_score, name="get_score"),
    re_path(r"^authenticate/", CustomObtainAuthToken.as_view()),
    re_path(r"^api/v1/createwallet/$", create_wallet, name="create_wallet"),
    re_path(r"^api/v1/count/$", issue_count, name="api_count"),
    re_path(r"^api/v1/contributors/$", contributors, name="api_contributor"),
    path("projects/<slug:slug>/badge/", ProjectBadgeView.as_view(), name="project-badge"),
    path("repos/<slug:slug>/badge/", RepoBadgeView.as_view(), name="repo-badge"),
    path("repository/<slug:slug>/", RepoDetailView.as_view(), name="repo_detail"),
    re_path(r"^report-ip/$", ReportIpView.as_view(), name="report_ip"),
    re_path(r"^reported-ips/$", ReportedIpListView.as_view(), name="reported_ips_list"),
    re_path(r"^feed/$", feed, name="feed"),
    re_path(
        r"^api/v1/createissues/$",
        csrf_exempt(IssueCreate.as_view()),
        name="issuecreate",
    ),
    re_path(
        r"^api/v1/search/$",
        csrf_exempt(search_issues),
        name="search_issues",
    ),
    re_path(
        r"^api/v1/delete_issue/(?P<id>\w+)/$",
        csrf_exempt(delete_issue),
        name="delete_api_issue",
    ),
    re_path(
        r"^api/v1/remove_user_from_issue/(?P<id>\w+)/$",
        csrf_exempt(remove_user_from_issue),
        name="remove_api_user_from_issue",
    ),
    re_path(
        r"^api/v1/issue/update/$",
        csrf_exempt(UpdateIssue),
        name="update_api_issue",
    ),
    re_path(r"^api/v1/scoreboard/$", get_scoreboard, name="api_scoreboard"),
    re_path(
        r"^api/v1/terms/$",
        csrf_exempt(TemplateView.as_view(template_name="mobile_terms.html")),
        name="api_terms",
    ),
    re_path(
        r"^api/v1/about/$",
        csrf_exempt(TemplateView.as_view(template_name="mobile_about.html")),
        name="api_about",
    ),
    re_path(
        r"^api/v1/privacypolicy/$",
        csrf_exempt(TemplateView.as_view(template_name="mobile_privacy.html")),
        name="api_privacypolicy",
    ),
    re_path(
        r"^contribute/$",
        ContributeView.as_view(),
        name="contribution_guidelines",
    ),
    path("select_contribution/", select_contribution, name="select_contribution"),
    path(
        "distribute_bacon/<int:contribution_id>/",
        distribute_bacon,
        name="distribute_bacon",
    ),
    path("activity/like/<int:id>/", like_activity, name="like_activity"),
    path("activity/dislike/<int:id>/", dislike_activity, name="dislike_activity"),
    path("activity/approve/<int:id>/", approve_activity, name="approve_activity"),
    re_path(r"^tz_detect/", include("tz_detect.urls")),
    re_path(r"^ratings/", include("star_ratings.urls", namespace="ratings")),
    re_path(r"^robots\.txt$", robots_txt),
    re_path(r"^contributors/$", contributors_view, name="contributors"),
    # users
    path("users/", users_view, name="users"),
    # company specific urls :
    path(
        "organization/",
        RegisterOrganizationView.as_view(),
        name="register_organization",
    ),
    path("organization/dashboard/", Organization_view, name="organization_view"),
    path(
        "organization/<int:id>/dashboard/analytics/",
        OrganizationDashboardAnalyticsView.as_view(),
        name="organization_analytics",
    ),
    path(
        "organization/<int:id>/dashboard/integrations/",
        OrganizationDashboardIntegrations.as_view(),
        name="organization_manage_integrations",
    ),
    path(
        "organization/<int:id>/dashboard/bugs/",
        OrganizationDashboardManageBugsView.as_view(),
        name="organization_manage_bugs",
    ),
    path(
        "organization/<int:id>/dashboard/team-overview/",
        OrganizationDashboardTeamOverviewView.as_view(),
        name="organization_team_overview",
    ),
    path(
        "organization/<int:id>/dashboard/domains/",
        OrganizationDashboardManageDomainsView.as_view(),
        name="organization_manage_domains",
    ),
    path(
        "organization/<int:id>/dashboard/roles/",
        OrganizationDashboardManageRolesView.as_view(),
        name="organization_manage_roles",
    ),
    path(
        "organization/<int:id>/dashboard/bughunts/",
        OrganizationDashboardManageBughuntView.as_view(),
        name="organization_manage_bughunts",
    ),
    path(
        "organization/dashboard/end_bughunt/<int:pk>",
        EndBughuntView.as_view(),
        name="end_bughunt",
    ),
    path(
        "organization/<int:id>/dashboard/add_bughunt/",
        AddHuntView.as_view(),
        name="add_bughunt",
    ),
    path(
        "organization/<int:id>/dashboard/add_domain/",
        AddDomainView.as_view(),
        name="add_domain",
    ),
    path(
        "organization/<int:id>/dashboard/add_slack_integration/",
        AddSlackIntegrationView.as_view(),
        name="add_slack_integration",
    ),
    path(
        "organization/<int:id>/dashboard/edit_domain/<int:domain_id>/",
        AddDomainView.as_view(),
        name="edit_domain",
    ),
    path(
        "organization/domain/<int:pk>/",
        login_required(DomainView.as_view()),
        name="view_domain",
    ),
    path(
        "organization/delete_prize/<int:prize_id>/<int:organization_id>",
        delete_prize,
        name="delete_prize",
    ),
    path(
        "organization/edit_prize/<int:prize_id>/<int:organization_id>",
        edit_prize,
        name="edit_prize",
    ),
    path(
        "organization/accept_bug/<int:issue_id>/<str:reward_id>/",
        accept_bug,
        name="accept_bug",
    ),
    path(
        "organization/accept_bug/<int:issue_id>/<str:no_reward>/",
        accept_bug,
        name="accept_bug_no_reward",
    ),
    path(
        "organization/delete_manager/<int:manager_id>/<int:domain_id>/",
        delete_manager,
        name="delete_manager",
    ),
    path("features/", features_view, name="features"),
    path("sponsor/", sponsor_view, name="sponsor"),
    path("donate/", donate_view, name="donate"),
    path("organizations/", OrganizationListView.as_view(), name="organizations"),
    path("map/", MapView.as_view(), name="map"),
    path("domains/", DomainListView.as_view(), name="domains"),
    path("trademarks/", trademark_search, name="trademark_search"),
    path(
        "generate_bid_image/<int:bid_amount>/",
        generate_bid_image,
        name="generate_bid_image",
    ),
    path("bidding/", SaveBiddingData, name="BiddingData"),
    path("select_bid/", select_bid, name="select_bid"),
    path("get_unique_issues/", get_unique_issues, name="get_unique_issues"),
    path("change_bid_status/", change_bid_status, name="change_bid_status"),
    path("fetch-current-bid/", fetch_current_bid, name="fetch_current_bid"),
    path("Submitpr/", submit_pr, name="submit_pr"),
    path("weekly-report/", weekly_report, name="weekly_report"),
    path("forum/add/", add_forum_post, name="add_forum_post"),
    path("forum/", view_forum, name="view_forum"),
    path("forum/vote/", vote_forum_post, name="vote_forum_post"),
    path("forum/set-vote-status/", set_vote_status, name="set_vote_status"),
    path("forum/comment/", add_forum_comment, name="add_forum_comment"),
    re_path(
        r"^trademarks/query=(?P<slug>[\w\s\W]+)$",
        trademark_detailview,
        name="trademark_detailview",
    ),
    path(
        "update_bch_address/",
        update_bch_address,
        name="update_bch_address",
    ),
    # path(
    #     "api/chatbot/conversation/", chatbot_conversation, name="chatbot_conversation"
    # ),
    path("blt-tomato/", blt_tomato, name="blt-tomato"),
    path(
        "api/v1/projects/",
        ProjectViewSet.as_view({"get": "list", "post": "create", "patch": "update"}),
        name="projects_api",
    ),
    path(
        "auth/delete",
        AuthApiViewset.as_view({"delete": "delete"}),
        name="auth-delete-api",
    ),
    path(
        "api/v1/tags",
        TagApiViewset.as_view({"get": "list", "post": "create"}),
        name="tags-api",
    ),
    path("sizzle/", sizzle, name="sizzle"),
    path("check-in/", checkIN, name="checkIN"),
    path("add-sizzle-checkin/", add_sizzle_checkIN, name="add_sizzle_checkin"),
    path("check-in/<int:report_id>/", checkIN_detail, name="checkIN_detail"),
    path("sizzle-docs/", sizzle_docs, name="sizzle-docs"),
    path("api/timelogsreport/", TimeLogListAPIView, name="timelogsreport"),
    path("time-logs/", TimeLogListView, name="time_logs"),
    path("sizzle-daily-log/", sizzle_daily_log, name="sizzle_daily_log"),
    path(
        "user-sizzle-report/<str:username>/",
        user_sizzle_report,
        name="user_sizzle_report",
    ),
    path("submit-roadmap-pr/", submit_roadmap_pr, name="submit-roadmap-pr"),
    path("view-pr-analysis/", view_pr_analysis, name="view_pr_analysis"),
    path("delete_time_entry/", delete_time_entry, name="delete_time_entry"),
    path("assign-badge/<str:username>/", assign_badge, name="assign_badge"),
    path("github-webhook/", github_webhook, name="github-webhook"),
    # blog urls
    path("blog/", PostListView.as_view(), name="post_list"),
    path("blog/new/", PostCreateView.as_view(), name="post_form"),
    path("blog/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("blog/<slug:slug>/edit/", PostUpdateView.as_view(), name="post_update"),
    path("blog/<slug:slug>/delete/", PostDeleteView.as_view(), name="post_delete"),
    # gamification related urls
    path("teams/overview/", TeamOverview.as_view(), name="team_overview"),
    path("teams/search-users/", search_users, name="search_users"),
    path("teams/create-team/", create_team, name="create_team"),
    path("teams/join-requests/", join_requests, name="join_requests"),
    path("teams/add-member/", add_member, name="add_member"),
    path("teams/delete-team/", delete_team, name="delete_team"),
    path("teams/leave-team/", leave_team, name="leave_team"),
    path("teams/kick-member/", kick_member, name="kick_member"),
    path("teams/give-kudos/", give_kudos, name="give_kudos"),
    path(
        "similarity_scan/",
        TemplateView.as_view(template_name="similarity_scan.html"),
        name="similarity_scan",
    ),
    path("projects/create/", create_project, name="create_project"),
    path("teams/challenges/", TeamChallenges.as_view(), name="team_challenges"),
    path("teams/leaderboard/", TeamLeaderboard.as_view(), name="team_leaderboard"),
    path("user_challenges/", UserChallengeListView.as_view(), name="user_challenges"),
    path("project/<slug:slug>/", ProjectsDetailView.as_view(), name="project_detail"),
    path("slack/events", slack_events, name="slack_events"),
    path("owasp/", TemplateView.as_view(template_name="owasp.html"), name="owasp"),
    path("discussion-rooms/", RoomsListView.as_view(), name="rooms_list"),
    path("discussion-rooms/create/", RoomCreateView.as_view(), name="room_create"),
    path("discussion-rooms/join-room/<int:room_id>/", join_room, name="join_room"),
    path("discussion-rooms/delete-room/<int:room_id>/", delete_room, name="delete_room"),
    path(
        "batch-send-bacon-tokens/",
        batch_send_bacon_tokens_view,
        name="batch_send_bacon_tokens",
    ),
    path("pending-transactions/", pending_transactions_view, name="pending_transactions"),
    path("open-source-sorting-hat/", ossh_home, name="ossh_home"),
    path("open-source-sorting-hat/results", ossh_results, name="ossh_results"),
    path("get-github-data/", get_github_data, name="get_github_data"),
    path("get-recommended-repos/", get_recommended_repos, name="get_recommended_repos"),
    path("get-recommended-communities/", get_recommended_communities, name="get_recommended_communities"),
    path(
        "get-recommended-discussion-channels/",
        get_recommended_discussion_channels,
        name="get_recommended_discussion_channels",
    ),
    path("get-recommended-articles/", get_recommended_articles, name="get_recommended_articles"),
    path("stats-dashboard/", stats_dashboard, name="stats_dashboard"),
    path("stats/sync-github-projects/", sync_github_projects, name="sync_github_projects"),
    path("stats/run-command/", run_management_command, name="run_management_command"),
    path("test-sentry/", test_sentry, name="test_sentry"),
    path("template_list/", template_list, name="template_list"),
    path(
        "github-issue-prompt/",
        TemplateView.as_view(template_name="github_issue_prompt.html"),
        name="github_issue_prompt",
    ),
    path("check_owasp_compliance/", check_owasp_compliance, name="check_owasp_compliance"),
    path("create-github-issue/", GithubIssueView.as_view(), name="create_github_issue"),
    path("get-github-issue/", get_github_issue, name="get_github_issue"),
    # path("api/v1/owasp-compliance/", views.OwaspComplianceChecker.as_view(), name="owasp-compliance-check"),
    path("repo_list/", RepoListView.as_view(), name="repo_list"),
    path("add_repo", add_repo, name="add_repo"),
    path("organization/<slug:slug>/", OrganizationDetailView.as_view(), name="organization_detail"),
    path("organization/<slug:slug>/update-repos/", update_organization_repos, name="update_organization_repos"),
    # GitHub Issues
    path("github-issues/<int:pk>/", GitHubIssueDetailView.as_view(), name="github_issue_detail"),
    path("github-issues/", GitHubIssuesView.as_view(), name="github_issues"),
    path("api/bacon/submit/", BaconSubmissionView.as_view(), name="bacon_submit"),
    path("bacon-requests/", bacon_requests_view, name="bacon_requests"),
    path("update-submission-status/<int:submission_id>/", update_submission_status, name="update_submission_status"),
    path("initiate-transaction/", initiate_transaction, name="initiate_transaction"),
    path("api/get-wallet-balance/", get_wallet_balance, name="get_wallet_balance"),
    path("extension/", TemplateView.as_view(template_name="extension.html"), name="extension"),
    path("domains/<int:domain_id>/check-security/", check_domain_security, name="check_domain_security"),
    path("roadmap/", RoadmapView.as_view(), name="roadmap"),
    path("page-vote/", page_vote, name="page_vote"),
    # Queue Management URLs
    path("queue/", queue_list, name="queue_list"),
    path("queue/create/", queue_list, name="queue_create"),
    path("queue/<int:queue_id>/edit/", queue_list, name="queue_edit"),
    path("queue/<int:queue_id>/delete/", queue_list, name="queue_delete"),
    path("queue/<int:queue_id>/launch/", queue_list, name="queue_launch"),
    path("queue/launch-control/", queue_list, name="queue_launch_page"),
    # Chat room API endpoints
    path("api/send-message/", send_message_api, name="send_message_api"),
    path("api/room-messages/<int:room_id>/", room_messages_api, name="room_messages_api"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        re_path(r"^__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
