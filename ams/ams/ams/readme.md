User Manual

Start the server at: cd run_waitress.py> with CMD "waitress-serve --port=80 ams.wsgi:application"

1. OAuth Login/Signup

RL: https://d2xtaexzsbvmol.cloudfront.net/

Here, you can log in or sign up using OAuth (e.g., Google).

To access the application, start by selecting your role:

URL: https://d2xtaexzsbvmol.cloudfront.net/role-selection/

2. Successful Signup/Redirect
After a successful signup or login, you will be redirected to  URL: https://d2xtaexzsbvmol.cloudfront.net/accounts/profile then navigate to URL: https://d2xtaexzsbvmol.cloudfront.net/accounts/ you will see the status of your signin!


3. Choose Your Role
You will be prompted to select your role:

URL: https://d2xtaexzsbvmol.cloudfront.net/role-selection/

Note: If you choose to act as an admin for performing CRUD (Create, Read, Update, Delete) operations, you will need to enter the admin code: admin007.

4. View Articles
After selecting your role, you can view the list of articles. If you are an admin, you will see additional options for editing and deleting articles.

URL: https://d2xtaexzsbvmol.cloudfront.net/



5. Create Article
Admins can create new articles by navigating to the create article page:

URL: https://d2xtaexzsbvmol.cloudfront.net/article/create/



6. Edit Article
To edit an existing article, navigate to the edit article page. Replace <int:pk> with the specific ID of the article you want to edit:

URL: https://d2xtaexzsbvmol.cloudfront.net/article/int:pk/update/


7. Delete Article
To delete an existing article, navigate to the delete article page. Replace <int:pk> with the specific ID of the article you want to delete:

URL: https://d2xtaexzsbvmol.cloudfront.net/article/int:pk/delete/


Note:
Admin Privileges: Only users with admin privileges (who have correctly entered the admin code) will have the ability to create, edit, or delete articles.

Session Persistence: Ensure your session is active to perform admin operations; otherwise, you might need to reselect your role.
This manual guides you through accessing the various features of your application, from login to article management.




#API endpoints:

/       articles.views.ArticleListView  article_list
/accounts/3rdparty/     allauth.socialaccount.views.ConnectionsView     socialaccount_connections
/accounts/3rdparty/login/cancelled/     allauth.socialaccount.views.LoginCancelledView  socialaccount_login_cancelled
/accounts/3rdparty/login/error/ allauth.socialaccount.views.LoginErrorView      socialaccount_login_error
/accounts/3rdparty/signup/      allauth.socialaccount.views.SignupView  socialaccount_signup
/accounts/confirm-email/        allauth.account.views.email_verification_sent   account_email_verification_sent
/accounts/confirm-email/<key>/  allauth.account.views.ConfirmEmailView  account_confirm_email
/accounts/email/        allauth.account.views.EmailView account_email
/accounts/google/login/ allauth.socialaccount.providers.oauth2.views.view       google_login
/accounts/google/login/callback/        allauth.socialaccount.providers.oauth2.views.view       google_callback
/accounts/google/login/token/   allauth.socialaccount.providers.google.views.LoginByTokenView   google_login_by_token
/accounts/inactive/     allauth.account.views.AccountInactiveView       account_inactive
/accounts/login/        allauth.account.views.LoginView account_login
/accounts/login/code/confirm/   allauth.account.views.ConfirmLoginCodeView      account_confirm_login_code
/accounts/logout/       allauth.account.views.LogoutView        account_logout
/accounts/password/change/      allauth.account.views.PasswordChangeView        account_change_password
/accounts/password/reset/       allauth.account.views.PasswordResetView account_reset_password
/accounts/password/reset/done/  allauth.account.views.PasswordResetDoneView     account_reset_password_done
/accounts/password/reset/key/<uidb36>-<key>/    allauth.account.views.PasswordResetFromKeyView  account_reset_password_from_key
/accounts/password/reset/key/done/      allauth.account.views.PasswordResetFromKeyDoneView      account_reset_password_from_key_done
/accounts/password/set/ allauth.account.views.PasswordSetView   account_set_password
/accounts/reauthenticate/       allauth.account.views.ReauthenticateView        account_reauthenticate
/accounts/signup/       allauth.account.views.SignupView        account_signup
/accounts/social/connections/   django.views.generic.base.RedirectView
/accounts/social/login/cancelled/       django.views.generic.base.RedirectView
/accounts/social/login/error/   django.views.generic.base.RedirectView
/accounts/social/signup/        django.views.generic.base.RedirectView
/admin/ django.contrib.admin.sites.index        admin:index
/admin/<app_label>/     django.contrib.admin.sites.app_index    admin:app_list
/admin/<url>    django.contrib.admin.sites.catch_all_view
/admin/account/emailaddress/    django.contrib.admin.options.changelist_view    admin:account_emailaddress_changelist
/admin/account/emailaddress/<path:object_id>/   django.views.generic.base.RedirectView
/admin/account/emailaddress/<path:object_id>/change/    django.contrib.admin.options.change_view        admin:account_emailaddress_change
/admin/account/emailaddress/<path:object_id>/delete/    django.contrib.admin.options.delete_view        admin:account_emailaddress_delete
/admin/account/emailaddress/<path:object_id>/history/   django.contrib.admin.options.history_view       admin:account_emailaddress_history
/admin/account/emailaddress/add/        django.contrib.admin.options.add_view   admin:account_emailaddress_add
/admin/auth/group/      django.contrib.admin.options.changelist_view    admin:auth_group_changelist
/admin/auth/group/<path:object_id>/     django.views.generic.base.RedirectView
/admin/auth/group/<path:object_id>/change/      django.contrib.admin.options.change_view        admin:auth_group_change
/admin/auth/group/<path:object_id>/delete/      django.contrib.admin.options.delete_view        admin:auth_group_delete
/admin/auth/group/<path:object_id>/history/     django.contrib.admin.options.history_view       admin:auth_group_history
/admin/auth/group/add/  django.contrib.admin.options.add_view   admin:auth_group_add
/admin/auth/user/       django.contrib.admin.options.changelist_view    admin:auth_user_changelist
/admin/auth/user/<id>/password/ django.contrib.auth.admin.user_change_password  admin:auth_user_password_change
/admin/auth/user/<path:object_id>/      django.views.generic.base.RedirectView
/admin/auth/user/<path:object_id>/change/       django.contrib.admin.options.change_view        admin:auth_user_change
/admin/auth/user/<path:object_id>/delete/       django.contrib.admin.options.delete_view        admin:auth_user_delete
/admin/auth/user/<path:object_id>/history/      django.contrib.admin.options.history_view       admin:auth_user_history
/admin/auth/user/add/   django.contrib.auth.admin.add_view      admin:auth_user_add
/admin/autocomplete/    django.contrib.admin.sites.autocomplete_view    admin:autocomplete
/admin/jsi18n/  django.contrib.admin.sites.i18n_javascript      admin:jsi18n
/admin/login/   django.contrib.admin.sites.login        admin:login
/admin/logout/  django.contrib.admin.sites.logout       admin:logout
/admin/password_change/ django.contrib.admin.sites.password_change      admin:password_change
/admin/password_change/done/    django.contrib.admin.sites.password_change_done admin:password_change_done
/admin/r/<int:content_type_id>/<path:object_id>/        django.contrib.contenttypes.views.shortcut      admin:view_on_site
/admin/sites/site/      django.contrib.admin.options.changelist_view    admin:sites_site_changelist
/admin/sites/site/<path:object_id>/     django.views.generic.base.RedirectView
/admin/sites/site/<path:object_id>/change/      django.contrib.admin.options.change_view        admin:sites_site_change
/admin/sites/site/<path:object_id>/delete/      django.contrib.admin.options.delete_view        admin:sites_site_delete
/admin/sites/site/<path:object_id>/history/     django.contrib.admin.options.history_view       admin:sites_site_history
/admin/sites/site/add/  django.contrib.admin.options.add_view   admin:sites_site_add
/admin/socialaccount/socialaccount/     django.contrib.admin.options.changelist_view    admin:socialaccount_socialaccount_changelist
/admin/socialaccount/socialaccount/<path:object_id>/    django.views.generic.base.RedirectView
/admin/socialaccount/socialaccount/<path:object_id>/change/     django.contrib.admin.options.change_view        admin:socialaccount_socialaccount_change   
/admin/socialaccount/socialaccount/<path:object_id>/delete/     django.contrib.admin.options.delete_view        admin:socialaccount_socialaccount_delete   
/admin/socialaccount/socialaccount/<path:object_id>/history/    django.contrib.admin.options.history_view       admin:socialaccount_socialaccount_history  
/admin/socialaccount/socialaccount/add/ django.contrib.admin.options.add_view   admin:socialaccount_socialaccount_add
/admin/socialaccount/socialapp/ django.contrib.admin.options.changelist_view    admin:socialaccount_socialapp_changelist
/admin/socialaccount/socialapp/<path:object_id>/        django.views.generic.base.RedirectView
/admin/socialaccount/socialapp/<path:object_id>/change/ django.contrib.admin.options.change_view        admin:socialaccount_socialapp_change
/admin/socialaccount/socialapp/<path:object_id>/delete/ django.contrib.admin.options.delete_view        admin:socialaccount_socialapp_delete
/admin/socialaccount/socialapp/<path:object_id>/history/        django.contrib.admin.options.history_view       admin:socialaccount_socialapp_history      
/admin/socialaccount/socialapp/add/     django.contrib.admin.options.add_view   admin:socialaccount_socialapp_add
/admin/socialaccount/socialtoken/       django.contrib.admin.options.changelist_view    admin:socialaccount_socialtoken_changelist
/admin/socialaccount/socialtoken/<path:object_id>/      django.views.generic.base.RedirectView
/admin/socialaccount/socialtoken/<path:object_id>/change/       django.contrib.admin.options.change_view        admin:socialaccount_socialtoken_change     
/admin/socialaccount/socialtoken/<path:object_id>/delete/       django.contrib.admin.options.delete_view        admin:socialaccount_socialtoken_delete     
/admin/socialaccount/socialtoken/<path:object_id>/history/      django.contrib.admin.options.history_view       admin:socialaccount_socialtoken_history    
/admin/socialaccount/socialtoken/add/   django.contrib.admin.options.add_view   admin:socialaccount_socialtoken_add
/api/   rest_framework.routers.APIRootView      api-root
/api/   rest_framework.routers.APIRootView      api-root
/api/\.<format>/        rest_framework.routers.APIRootView      api-root
/api/\.<format>/        rest_framework.routers.APIRootView      api-root
/api/api/articles/      articles.views.ArticleViewSet   article-list
/api/api/articles/<pk>/ articles.views.ArticleViewSet   article-detail
/api/api/articles/<pk>\.<format>/       articles.views.ArticleViewSet   article-detail
/api/api/articles\.<format>/    articles.views.ArticleViewSet   article-list
/api/api/tags/  articles.views.TagViewSet       tag-list
/api/api/tags/<pk>/     articles.views.TagViewSet       tag-detail
/api/api/tags/<pk>\.<format>/   articles.views.TagViewSet       tag-detail
/api/api/tags\.<format>/        articles.views.TagViewSet       tag-list
/api/api/users/ articles.views.UserViewSet      user-list
/api/api/users/<pk>/    articles.views.UserViewSet      user-detail
/api/api/users/<pk>\.<format>/  articles.views.UserViewSet      user-detail
/api/api/users\.<format>/       articles.views.UserViewSet      user-list
/api/articles/  articles.views.ArticleViewSet   article-list
/api/articles/<pk>/     articles.views.ArticleViewSet   article-detail
/api/articles/<pk>\.<format>/   articles.views.ArticleViewSet   article-detail
/api/articles\.<format>/        articles.views.ArticleViewSet   article-list
/api/tags/      articles.views.TagViewSet       tag-list
/api/tags/<pk>/ articles.views.TagViewSet       tag-detail
/api/tags/<pk>\.<format>/       articles.views.TagViewSet       tag-detail
/api/tags\.<format>/    articles.views.TagViewSet       tag-list
/article/<int:pk>/delete/       articles.views.ArticleDeleteView        article_delete
/article/<int:pk>/update/       articles.views.ArticleUpdateView        article_update
/article/create/        articles.views.ArticleCreateView        article_create
/role-selection/        articles.views.role_selection_view      role_selection
/verify-admin-code/     articles.views.AdminCodeVerificationView        verify_admin_code







