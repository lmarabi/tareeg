/*
 * timeval.h    1.3 2003/01/14
 *
 * Defines gettimeofday, timeval, etc. for Win32
 *
 * By Wu Yongwei
 *
 */

#ifndef _TIMEVAL_H
#define _TIMEVAL_H

#ifdef _WIN32

#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif

#include <winsock2.h>
#include <time.h>

#if defined(_MSC_VER) || defined(__BORLANDC__)
#define EPOCHFILETIME (116444736000000000i64)
#else
#define EPOCHFILETIME (116444736000000000LL)
#endif

struct timezone {
    int tz_minuteswest; /* minutes W of Greenwich */
    int tz_dsttime;     /* type of dst correction */
};

#endif /* _WIN32 */

/* For MingW the appropriate definitions are included in
 time.h but they are not included if __STRICT_ANSI__
 is defined.  Since GEOS is compiled with -ansi that
 means the definitions are not available. */
#if defined(_WIN32) && defined(__GNUC__)
extern _CRTIMP void __cdecl    _tzset (void);
__MINGW_IMPORT int    _daylight;
__MINGW_IMPORT long    _timezone;
#endif 

#if defined(_WIN32) && !defined(_WIN32_WCE)

__inline int gettimeofday(struct timeval *tv, struct timezone *tz)
{
    FILETIME        ft;
    LARGE_INTEGER   li;
    __int64         t;
    static int      tzflag;

    if (tv)
    {
        GetSystemTimeAsFileTime(&ft);
        li.LowPart  = ft.dwLowDateTime;
        li.HighPart = ft.dwHighDateTime;
        t  = li.QuadPart;       /* In 100-nanosecond intervals */
        t -= EPOCHFILETIME;     /* Offset to the Epoch time */
        t /= 10;                /* In microseconds */
        tv->tv_sec  = (long)(t / 1000000);
        tv->tv_usec = (long)(t % 1000000);
    }

    if (tz)
    {
        if (!tzflag)
        {
            _tzset();
            tzflag++;
        }
        tz->tz_minuteswest = _timezone / 60;
        tz->tz_dsttime = _daylight;
    }

    return 0;
}

#elif defined(_WIN32_WCE)

__inline int gettimeofday(struct timeval *tv, struct timezone *tz)
{
	SYSTEMTIME      st;
    FILETIME        ft;
    LARGE_INTEGER   li;
    TIME_ZONE_INFORMATION tzi;
    __int64         t;
    static int      tzflag;

    if (tv)
    {
		GetSystemTime(&st);
		SystemTimeToFileTime(&st, &ft);
        li.LowPart  = ft.dwLowDateTime;
        li.HighPart = ft.dwHighDateTime;
        t  = li.QuadPart;       /* In 100-nanosecond intervals */
        t -= EPOCHFILETIME;     /* Offset to the Epoch time */
        t /= 10;                /* In microseconds */
        tv->tv_sec  = (long)(t / 1000000);
        tv->tv_usec = (long)(t % 1000000);
    }

    if (tz)
    {   
        GetTimeZoneInformation(&tzi);
		
        tz->tz_minuteswest = tzi.Bias;
		if (tzi.StandardDate.wMonth != 0)
        {
			tz->tz_minuteswest += tzi.StandardBias * 60;
        }

        if (tzi.DaylightDate.wMonth != 0)
        {
            tz->tz_dsttime = 1;
        }
        else
        {
            tz->tz_dsttime = 0;
        }
    }

    return 0;
}

#else  /* _WIN32 */

#include <sys/time.h>

#endif /* _WIN32 */

#endif /* _TIMEVAL_H */
