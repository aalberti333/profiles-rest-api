from rest_framework import permissions

#permissions is a class DRF uses to determine if user has permission to make
#change they're asking

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""
    #there's a function (has object permission)
    #this is called every time a request is made to API
    #result determines whether uses does/doesn't have permission to return action
    #(will be true or false)

    def has_object_permission(self, request, view, obj):
        """check user is trying to edit their own profile"""

        #we don't need permissions if a user is trying to simply VIEW a profile
        #we can do this by checking a safe methods list
        #this is a HTTP method that is classified as safe (non destructive method)
        #allows you to retrieve, but not change/modify/delete
        #a safe method is HTTP GET

        #checks to see if request method is in the safe permissions of DRF
        if request.method in permissions.SAFE_METHODS:
            return True

        #check if user is trying to change THEIR OWN profile
        #this should be True, users should be allowed delete/update/change
        #their own profile


        #checks to see if the user trying to make changes is the same as the id
        #of the object trying to be changed
        return obj.id == request.user.id
