/*=============================================================================

    This file is part of ARB.

    ARB is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    ARB is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with ARB; if not, write to the Free Software
    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA

=============================================================================*/
/******************************************************************************

    Copyright (C) 2016 Pascal Molin

******************************************************************************/

#include "acb_dirichlet.h"
#include <math.h>
#define PI   3.14159265358
#define LOG2 0.69314718055

ulong
acb_dirichlet_theta_length_d(ulong q, double t, slong prec)
{
    double a, la;
    a = PI / (double)q * t * t;
    la = (a < .3) ? -log(2*a*(1-a)) : .8;
    la = ((double)prec * LOG2 + la) / a;
    return ceil(sqrt(la)+.5);
}

ulong
acb_dirichlet_theta_length(ulong q, const arb_t t, slong prec)
{
    double dt;
    ulong len;
    arf_t at;
    arf_init(at);
    arb_get_lbound_arf(at, t, 53);
    dt = arf_get_d(at, ARF_RND_DOWN);
    len = acb_dirichlet_theta_length_d(q, dt, prec);
    arf_clear(at);
    return len;
}
