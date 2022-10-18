import enum


class AuthType(enum.Enum):
    BASIC = 'basic'
    DIGEST = 'digest'
    DIGEST_CACHED = 'digest_cached'

    @classmethod
    def choices(cls) -> frozenset[str]:
        return frozenset(member.value for member in cls)


@enum.unique
class EndpointAddr(enum.Enum):
    ALERT_STREAM = 'ISAPI/Event/notification/alertStream'
    CHANNEL_CAPABILITIES = 'ISAPI/Image/channels/1/capabilities'
    EXPOSURE = 'ISAPI/Image/channels/1/exposure'
    IRCUT_FILTER = 'ISAPI/Image/channels/1/ircutFilter'
    INTRUSION_DETECTION = 'ISAPI/Smart/FieldDetection/1'
    LINE_CROSSING_DETECTION = 'ISAPI/Smart/LineDetection/1'
    MOTION_DETECTION = 'ISAPI/System/Video/inputs/channels/1/motionDetection'
    PICTURE = 'ISAPI/Streaming/channels/{channel}/picture?snapShotImageType=JPEG'


@enum.unique
class _BaseEndpointEnum(enum.Enum):
    def __str__(self) -> str:
        return str(self.value)


class IrcutFilterType(_BaseEndpointEnum):
    AUTO = 'auto'
    DAY = 'day'
    NIGHT = 'night'


class ExposureType(_BaseEndpointEnum):
    MANUAL = 'manual'


class OverexposeSuppressType(_BaseEndpointEnum):
    AUTO = 'AUTO'
    MANUAL = 'MANUAL'


class OverexposeSuppressEnabledType(_BaseEndpointEnum):
    TRUE = 'true'
    FALSE = 'false'
