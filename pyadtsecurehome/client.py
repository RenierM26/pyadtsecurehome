"""ADT Secure Home API."""
from __future__ import annotations

import logging
from typing import Any
from .exceptions import PyAdtSecureHomeError, InvalidURL, HTTPError
from .constants import DEFAULT_TIMEOUT, REQUEST_HEADER, STD_PARAMS

import requests

_LOGGER = logging.getLogger(__name__)

BASE_URL = "ids.trintel.co.za/Inhep-Impl-1.0-SNAPSHOT/"
API_ENDPOINT_LOGIN = "/auth/login"
API_ENDPOINT_CHECK_APP_VERSION = "/auth/checkAppVersion"
API_ENDPOINT_SITE_NOTIFICATIONS = "/device/getSiteNotifications"
API_ENDPOINT_SYNC_INFO = "/device/getSyncInfo"
API_ENDPOINT_STATE_INFO = "/device/getStateInfo"
API_ENDPOINT_NOTIFICATION_SUBSCRIPTIONS = "/device/getNotificationSubscriptions"
API_ENDPOINT_GET_USER_PREFERANCES = "/user/getUserPreferences"
API_ENDPOINT_SET_USER_PREFERANCE = "/user/setUserPreference"
API_ENDPOINT_SECURITY_COMPANIES = "/security-companies/list"
API_ENDPOINT_STORE_GCM_REGISTRATION_ID = "/user/storeGcmRegistrationId"
API_ENDPOINT_ARM_SITE = "/device/armSite"


class PyAdtSecureHome:
    """Initialize api client object."""

    def __init__(
        self,
        email: str | None = None,
        password: str | None = None,
        timeout: int = DEFAULT_TIMEOUT,
        token: str | None = None,
    ) -> None:
        """Initialize the client object."""
        self._email = email
        self._password = password
        self._session = None
        self.close_session()
        self._token = token
        self._timeout = timeout

    def login(self) -> dict[Any, Any]:
        """Login to ADT Secure Home API."""

        _params = STD_PARAMS
        _params["email"] = self._email
        _params["password"] = self._password

        try:
            req = self._session.get(
                "https://" + BASE_URL + API_ENDPOINT_LOGIN,
                allow_redirects=False,
                params=_params,
                timeout=self._timeout,
            )

            req.raise_for_status()

        except requests.ConnectionError as err:
            raise InvalidURL("A Invalid URL or Proxy error occured") from err

        except requests.HTTPError as err:
            raise HTTPError from err

        try:
            _json_result = req.json()

        except ValueError as err:
            raise PyAdtSecureHomeError(
                "Impossible to decode response: "
                + str(err)
                + "\nResponse was: "
                + str(req.text)
            ) from err

        if _json_result["status"] != "SUCCESS":
            raise PyAdtSecureHomeError(f"Login error: {_json_result}")

        self._token = _json_result["token"]

        return _json_result

    def check_app_version(self) -> dict[Any, Any]:
        """Check App version via API."""

        _params = STD_PARAMS
        _params["token"] = self._token
        _params["clientImei"] = STD_PARAMS["imei"]

        try:
            req = self._session.get(
                "https://" + BASE_URL + API_ENDPOINT_CHECK_APP_VERSION,
                allow_redirects=False,
                params=_params,
                timeout=self._timeout,
            )

            req.raise_for_status()

        except requests.ConnectionError as err:
            raise InvalidURL("A Invalid URL or Proxy error occured") from err

        except requests.HTTPError as err:
            raise HTTPError from err

        try:
            _json_result = req.json()

        except ValueError as err:
            raise PyAdtSecureHomeError(
                "Impossible to decode response: "
                + str(err)
                + "\nResponse was: "
                + str(req.text)
            ) from err

        if _json_result["status"] != "SUCCESS":
            raise PyAdtSecureHomeError(
                f"Error checking app version from api: {_json_result}"
            )

        return _json_result

    def site_notifications(self) -> dict[Any, Any]:
        """Get site notifications from API."""

        _params = STD_PARAMS
        _params["token"] = self._token

        try:
            req = self._session.get(
                "https://" + BASE_URL + API_ENDPOINT_SITE_NOTIFICATIONS,
                allow_redirects=False,
                params=_params,
                timeout=self._timeout,
            )

            req.raise_for_status()

        except requests.ConnectionError as err:
            raise InvalidURL("A Invalid URL or Proxy error occured") from err

        except requests.HTTPError as err:
            raise HTTPError from err

        try:
            _json_result = req.json()

        except ValueError as err:
            raise PyAdtSecureHomeError(
                "Impossible to decode response: "
                + str(err)
                + "\nResponse was: "
                + str(req.text)
            ) from err

        if _json_result["status"] != "SUCCESS":
            raise PyAdtSecureHomeError(
                f"Error getting site notifications from api: {_json_result}"
            )

        return _json_result

    def get_sync_info(self) -> dict[Any, Any]:
        """Get sync info from API."""

        _params = STD_PARAMS
        _params["token"] = self._token

        try:
            req = self._session.get(
                "https://" + BASE_URL + API_ENDPOINT_SYNC_INFO,
                allow_redirects=False,
                params=_params,
                timeout=self._timeout,
            )

            req.raise_for_status()

        except requests.ConnectionError as err:
            raise InvalidURL("A Invalid URL or Proxy error occured") from err

        except requests.HTTPError as err:
            raise HTTPError from err

        try:
            _json_result = req.json()

        except ValueError as err:
            raise PyAdtSecureHomeError(
                "Impossible to decode response: "
                + str(err)
                + "\nResponse was: "
                + str(req.text)
            ) from err

        if _json_result["status"] != "SUCCESS":
            raise PyAdtSecureHomeError(
                f"Error getting sync info from api: {_json_result}"
            )

        return _json_result

    def get_state_info(self) -> dict[Any, Any]:
        """Get state info from API."""

        _params = STD_PARAMS
        _params["token"] = self._token

        try:
            req = self._session.get(
                "https://" + BASE_URL + API_ENDPOINT_STATE_INFO,
                allow_redirects=False,
                params=_params,
                timeout=self._timeout,
            )

            req.raise_for_status()

        except requests.ConnectionError as err:
            raise InvalidURL("A Invalid URL or Proxy error occured") from err

        except requests.HTTPError as err:
            raise HTTPError from err

        try:
            _json_result = req.json()

        except ValueError as err:
            raise PyAdtSecureHomeError(
                "Impossible to decode response: "
                + str(err)
                + "\nResponse was: "
                + str(req.text)
            ) from err

        if _json_result["status"] != "SUCCESS":
            raise PyAdtSecureHomeError(
                f"Error getting state info from api: {_json_result}"
            )

        return _json_result

    def get_notification_subscriptions(self) -> dict[Any, Any]:
        """Get notification subscriptions from API."""

        _params = STD_PARAMS
        _params["token"] = self._token

        try:
            req = self._session.get(
                "https://" + BASE_URL + API_ENDPOINT_NOTIFICATION_SUBSCRIPTIONS,
                allow_redirects=False,
                params=_params,
                timeout=self._timeout,
            )

            req.raise_for_status()

        except requests.ConnectionError as err:
            raise InvalidURL("A Invalid URL or Proxy error occured") from err

        except requests.HTTPError as err:
            raise HTTPError from err

        try:
            _json_result = req.json()

        except ValueError as err:
            raise PyAdtSecureHomeError(
                "Impossible to decode response: "
                + str(err)
                + "\nResponse was: "
                + str(req.text)
            ) from err

        if _json_result["status"] != "SUCCESS":
            raise PyAdtSecureHomeError(
                f"Error getting notification subscriptions: {_json_result}"
            )

        return _json_result

    def get_user_preferences(self) -> dict[Any, Any]:
        """Get user preferences from API."""

        _params = STD_PARAMS
        _params["token"] = self._token

        try:
            req = self._session.get(
                "https://" + BASE_URL + API_ENDPOINT_GET_USER_PREFERANCES,
                allow_redirects=False,
                params=_params,
                timeout=self._timeout,
            )

            req.raise_for_status()

        except requests.ConnectionError as err:
            raise InvalidURL("A Invalid URL or Proxy error occured") from err

        except requests.HTTPError as err:
            raise HTTPError from err

        try:
            _json_result = req.json()

        except ValueError as err:
            raise PyAdtSecureHomeError(
                "Impossible to decode response: "
                + str(err)
                + "\nResponse was: "
                + str(req.text)
            ) from err

        if _json_result["status"] != "SUCCESS":
            raise PyAdtSecureHomeError(
                f"Error getting user preferences: {_json_result}"
            )

        return _json_result

    def get_security_companies(self) -> dict[Any, Any]:
        """Get security companies from API."""

        _params = STD_PARAMS
        _params["token"] = self._token

        try:
            req = self._session.get(
                "https://" + BASE_URL + API_ENDPOINT_SECURITY_COMPANIES,
                allow_redirects=False,
                params=_params,
                timeout=self._timeout,
            )

            req.raise_for_status()

        except requests.ConnectionError as err:
            raise InvalidURL("A Invalid URL or Proxy error occured") from err

        except requests.HTTPError as err:
            raise HTTPError from err

        try:
            _json_result = req.json()

        except ValueError as err:
            raise PyAdtSecureHomeError(
                "Impossible to decode response: "
                + str(err)
                + "\nResponse was: "
                + str(req.text)
            ) from err

        if _json_result["status"] != "SUCCESS":
            raise PyAdtSecureHomeError(
                f"Failed to get security companies: {_json_result}"
            )

        return _json_result

    def store_gcm_registrationid(self, gcm_id: str = None) -> dict[Any, Any]:
        """Store gcmid."""

        _params = STD_PARAMS
        _params["token"] = self._token
        _params["gcmId"] = gcm_id

        try:
            req = self._session.post(
                "https://" + BASE_URL + API_ENDPOINT_STORE_GCM_REGISTRATION_ID,
                allow_redirects=False,
                params=_params,
                timeout=self._timeout,
            )

            req.raise_for_status()

        except requests.ConnectionError as err:
            raise InvalidURL("A Invalid URL or Proxy error occured") from err

        except requests.HTTPError as err:
            raise HTTPError from err

        try:
            _json_result = req.json()

        except ValueError as err:
            raise PyAdtSecureHomeError(
                "Impossible to decode response: "
                + str(err)
                + "\nResponse was: "
                + str(req.text)
            ) from err

        if _json_result["status"] != "SUCCESS":
            raise PyAdtSecureHomeError(f"Storing gcm id failed with: {_json_result}")

        return _json_result

    def set_user_preference(
        self,
        site_id: str = None,
        partition_id: str = None,
        new_code: int = None,
        store_for: str = None,
    ) -> dict[Any, Any]:
        """Set user code preferences."""

        if store_for not in ["Arm", "Bypass"]:
            raise PyAdtSecureHomeError(
                "Invalid selection, choose between Arm or Bypass"
            )

        _params = STD_PARAMS
        _params["token"] = self._token
        _params["siteId"] = site_id

        _params["name"] = (
            "site." + site_id + ".partition." + partition_id + ".storeFor" + store_for
        )

        _params["preference_value"] = new_code

        try:
            req = self._session.post(
                "https://" + BASE_URL + API_ENDPOINT_SET_USER_PREFERANCE,
                allow_redirects=False,
                params=_params,
                timeout=self._timeout,
            )

            req.raise_for_status()

        except requests.ConnectionError as err:
            raise InvalidURL("A Invalid URL or Proxy error occured") from err

        except requests.HTTPError as err:
            raise HTTPError from err

        try:
            _json_result = req.json()

        except ValueError as err:
            raise PyAdtSecureHomeError(
                "Impossible to decode response: "
                + str(err)
                + "\nResponse was: "
                + str(req.text)
            ) from err

        if _json_result["status"] != "SUCCESS":
            raise PyAdtSecureHomeError(
                f"Set user preferance failed with: {_json_result}"
            )

        return _json_result

    def arm_site(
        self,
        arm: bool = True,
        pin: int = None,
        partition_id: int = None,
        site_id: int = None,
    ) -> dict[Any, Any]:
        """Arm alarm via API."""

        _params = STD_PARAMS
        _params["token"] = self._token
        _params["arm"] = arm
        _params["pin"] = pin
        _params["partitionId"] = partition_id
        _params["siteId"] = site_id

        try:
            req = self._session.get(
                "https://" + BASE_URL + API_ENDPOINT_ARM_SITE,
                allow_redirects=False,
                params=_params,
                timeout=self._timeout,
            )

            req.raise_for_status()

        except requests.ConnectionError as err:
            raise InvalidURL("A Invalid URL or Proxy error occured") from err

        except requests.HTTPError as err:
            raise HTTPError from err

        try:
            _json_result = req.json()

        except ValueError as err:
            raise PyAdtSecureHomeError(
                "Impossible to decode response: "
                + str(err)
                + "\nResponse was: "
                + str(req.text)
            ) from err

        if _json_result["status"] != "SUCCESS":
            raise PyAdtSecureHomeError(f"Arm site failed: {_json_result}")

        return _json_result

    def logout(self) -> None:
        """Close ADT Secure Home session."""
        self.close_session()

    def close_session(self) -> None:
        """Clear current session."""
        if self._session:
            self._session.close()

        self._session = requests.session()
        self._session.headers.update(REQUEST_HEADER)  # Reset session.